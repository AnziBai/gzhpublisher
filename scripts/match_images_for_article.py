#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文章智能配图匹配器
功能：根据文章内容自动匹配合适的图片并插入
"""

import sys
import os
import json
import requests
import re
from pathlib import Path
from typing import List, Tuple, Dict

# Windows 控制台编码
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# GLM API配置
GLM_API_KEY = "f9761e349d4947b4b54ac77b51da78c5.kGF1NoHb0jkaASUm"
GLM_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"

def get_embedding(text: str) -> list:
    """获取文本的embedding向量"""
    url = f"{GLM_BASE_URL}/embeddings"
    headers = {
        "Authorization": f"Bearer {GLM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "embedding-3",
        "input": text
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)

    if response.status_code != 200:
        raise ValueError(f"GLM API错误 ({response.status_code}): {response.text}")

    data = response.json()
    return data["data"][0]["embedding"]

RERANK_MODEL = "glm-5.1-air"  # GLM-5.1 精排模型，可调整为其他版本


def rerank_with_glm(paragraph: str, candidates: List[Tuple[str, str, float, int]]) -> List[Tuple[str, str, float, int]]:
    """
    用 GLM-5.1 对 embedding 候选进行语义精排，选出最匹配的1张图。
    若精排失败则降级返回 embedding top-1。
    """
    if len(candidates) <= 1:
        return candidates

    candidate_names = "\n".join(
        [f"{i + 1}. {name}" for i, (_, name, _, _) in enumerate(candidates)]
    )
    prompt = (
        f"以下是一段量化交易文章的内容：\n\n{paragraph}\n\n"
        f"以下是可供配图的图片名称（来自《概率的朋友》）：\n{candidate_names}\n\n"
        f"请从以上图片中，选出最适合配在这段文字旁边的1张图片（若所有图片都不太相关则回复0）。"
        f"只需回复图片编号（一个数字），不需要解释。"
    )

    url = f"{GLM_BASE_URL}/chat/completions"
    headers = {"Authorization": f"Bearer {GLM_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": RERANK_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": 10,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code != 200:
            print(f"  ⚠ GLM精排API错误({resp.status_code})，降级使用embedding top-1")
            return candidates[:1]
        reply = resp.json()["choices"][0]["message"]["content"].strip()
        idx = int(reply) - 1  # 转为 0-based；若回复 0 则 idx=-1
        if idx == -1:
            return []  # 模型认为没有合适的图
        if 0 <= idx < len(candidates):
            return [candidates[idx]]
    except Exception as e:
        print(f"  ⚠ GLM精排异常({e})，降级使用embedding top-1")
    return candidates[:1]


def cosine_similarity(vec1: list, vec2: list) -> float:
    """计算余弦相似度"""
    import math

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)

def split_article_into_paragraphs(article: str) -> List[str]:
    """
    将文章分段
    返回：[(段落文本, 段落在原文中的位置)]
    """
    # 按双换行符分段
    paragraphs = re.split(r'\n\s*\n', article)

    # 过滤空段落，保留有实际内容的段落
    result = []
    for para in paragraphs:
        para = para.strip()
        # 跳过YAML frontmatter、标题、已有的图片
        if len(para) > 20 and not para.startswith('---') and not para.startswith('#') and not para.startswith('!['):
            result.append(para)

    return result

def match_images_for_article(
    article: str,
    image_index_path: str,
    top_k: int = 5,
    min_similarity: float = 0.3
) -> List[Tuple[str, str, float, int]]:
    """
    为文章匹配合适的图片

    参数：
    - article: 文章内容（Markdown格式）
    - image_index_path: 图片向量索引文件路径
    - top_k: 每段最多匹配几张图片
    - min_similarity: 最低相似度阈值

    返回：
    [(图片路径, 图片描述, 相似度, 建议插入位置)]
    """
    # 加载图片索引
    with open(image_index_path, 'r', encoding='utf-8') as f:
        image_index = json.load(f)

    print(f"已加载 {len(image_index)} 张图片的向量索引")

    # 分段
    paragraphs = split_article_into_paragraphs(article)
    print(f"文章共 {len(paragraphs)} 个段落")

    # 为每段匹配图片
    matched_images = []

    for i, para in enumerate(paragraphs):
        print(f"\n[段落 {i+1}/{len(paragraphs)}]")
        print(f"  内容: {para[:50]}...")

        # 生成段落向量
        try:
            para_embedding = get_embedding(para)
        except Exception as e:
            print(f"  ✗ 生成向量失败: {e}")
            continue

        # 计算与所有图片的相似度
        similarities = []
        for img_filename, img_data in image_index.items():
            similarity = cosine_similarity(para_embedding, img_data["embedding"])
            if similarity >= min_similarity:
                # 使用文件名（去扩展名）作为标注，而不是 description
                caption = os.path.splitext(img_data["filename"])[0]
                similarities.append((
                    img_data["path"],
                    caption,
                    similarity,
                    i  # 段落索引
                ))

        # 排序并取top_k
        similarities.sort(key=lambda x: x[2], reverse=True)
        top_matches = similarities[:top_k]

        if top_matches:
            # GLM-5.1 精排：从 top_k 候选中选出最匹配的1张
            print(f"  → GLM精排 {len(top_matches)} 个候选...")
            reranked = rerank_with_glm(para, top_matches)
            if reranked:
                img_path, img_desc, sim, _ = reranked[0]
                print(f"  ✓ 精排选定: {img_desc} (embedding相似度: {sim:.3f})")
                matched_images.append((img_path, img_desc, sim, i))
            else:
                print(f"  - GLM判定无合适配图，跳过")
        else:
            print(f"  - 无匹配图片（相似度均低于 {min_similarity}）")

    return matched_images

def insert_images_into_article(
    article: str,
    matched_images: List[Tuple[str, str, float, int]],
    max_images_per_article: int = 5
) -> str:
    """
    将匹配的图片插入到文章中

    策略：
    1. 检查文章中已有的图片，避免重复插入
    2. 按相似度排序，取top N张图片
    3. 在对应段落后插入图片
    4. 避免连续插入（至少间隔2个段落）
    """
    # 提取文章中已有的图片路径（同时匹配 Markdown ![]() 和 HTML <img src=""> 格式）
    existing_images = set()
    for match in re.finditer(r'!\[.*?\]\((.*?)\)|<img[^>]+src=["\']([^"\']+)["\']', article):
        img_path = match.group(1) or match.group(2)
        if img_path:
            # 标准化路径（统一使用正斜杠）
            img_path_normalized = img_path.replace("\\", "/")
            existing_images.add(img_path_normalized)

    if existing_images:
        print(f"文章中已有 {len(existing_images)} 张图片，将避免重复插入")

    # 过滤掉已存在的图片
    filtered_images = []
    for img_path, img_desc, sim, para_idx in matched_images:
        img_path_normalized = img_path.replace("\\", "/")
        if img_path_normalized not in existing_images:
            filtered_images.append((img_path, img_desc, sim, para_idx))
        else:
            print(f"  - 跳过已存在的图片: {img_desc}")

    # 按相似度排序
    filtered_images.sort(key=lambda x: x[2], reverse=True)

    # 取top N
    selected_images = filtered_images[:max_images_per_article]

    # 按段落位置排序（从后往前插入，避免位置偏移）
    selected_images.sort(key=lambda x: x[3], reverse=True)

    # 拆分原文所有块（保留标题、分隔线等）
    all_blocks = re.split(r'\n\s*\n', article)

    # 建立 content_paragraph_index → all_blocks_index 的映射
    # （与 split_article_into_paragraphs 使用相同的过滤条件）
    content_block_indices = []
    for block_idx, block in enumerate(all_blocks):
        stripped = block.strip()
        if len(stripped) > 20 and not stripped.startswith('---') and not stripped.startswith('#') and not stripped.startswith('!['):
            content_block_indices.append(block_idx)

    # 插入图片
    last_inserted_para = 999999  # 上次插入的段落索引（初始化为很大的数）
    inserted_count = 0
    for img_path, img_desc, sim, para_idx in selected_images:
        # 避免连续插入（至少间隔2个段落）
        # 因为是从后往前插入，所以判断条件是 last_inserted_para - para_idx >= 3
        if last_inserted_para - para_idx < 3:
            print(f"  - 跳过距离过近的图片: {img_desc} (段落{para_idx+1})")
            continue

        # 在段落后插入图片（操作 all_blocks 而非 paragraphs，保留标题/分隔线）
        if para_idx < len(content_block_indices):
            block_idx = content_block_indices[para_idx]
            # 转换为正斜杠路径（wenyan-mcp要求）
            img_path_normalized = img_path.replace("\\", "/")

            # 插入HTML img标签（wenyan-mcp可上传本地路径，但Markdown![]()格式会退化为文字）
            all_blocks[block_idx] += f'\n\n<img src="{img_path_normalized}" alt="{img_desc}" style="border-radius: 8px; max-width: 100%;" />'

            last_inserted_para = para_idx
            inserted_count += 1

            print(f"  ✓ 插入图片: {img_desc} (段落{para_idx+1}, 相似度{sim:.3f})")

    print(f"\n共插入 {inserted_count} 张图片")

    # 重新组合文章（all_blocks 包含完整原文结构）
    return "\n\n".join(all_blocks)

def main():
    if len(sys.argv) < 2:
        print("用法: python match_images_for_article.py <文章文件路径> [输出文件路径]")
        print("示例: python match_images_for_article.py article.md article_with_images.md")
        sys.exit(1)

    article_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else article_path.replace(".md", "_with_images.md")
    index_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "image_embeddings_index.json")

    # 读取文章
    with open(article_path, 'r', encoding='utf-8') as f:
        article = f.read()

    print(f"文章路径: {article_path}")
    print(f"文章长度: {len(article)} 字符")
    print()

    # 匹配图片
    matched_images = match_images_for_article(article, index_path, top_k=3, min_similarity=0.3)

    print(f"\n共匹配到 {len(matched_images)} 张图片")

    # 插入图片
    article_with_images = insert_images_into_article(article, matched_images, max_images_per_article=5)

    # 保存
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(article_with_images)

    print(f"\n✓ 已保存配图文章: {output_path}")

if __name__ == "__main__":
    main()
