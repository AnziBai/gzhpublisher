#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能配图一键脚本
用法：python auto_add_images.py <文章文件路径>
"""

import sys
import os
import re

# 添加scripts目录到路径
sys.path.insert(0, "C:/Users/anzib/gzhpublisher/scripts")

from match_images_for_article import match_images_for_article, insert_images_into_article


def extract_frontmatter(article: str):
    """提取YAML frontmatter，返回 (frontmatter_str, body_str)"""
    if article.startswith('---'):
        end = article.find('\n---', 3)
        if end != -1:
            frontmatter = article[:end + 4]  # 包含结尾的 ---
            body = article[end + 4:].lstrip('\n')
            return frontmatter, body
    return '', article


def update_cover_in_frontmatter(frontmatter: str, cover_path: str) -> str:
    """更新frontmatter中的cover字段（正斜杠格式）"""
    cover_path_normalized = cover_path.replace("\\", "/")
    if re.search(r'^cover:', frontmatter, re.MULTILINE):
        return re.sub(r'^cover:.*$', f'cover: {cover_path_normalized}', frontmatter, flags=re.MULTILINE)
    else:
        # 在结尾 --- 前插入
        return frontmatter.replace('\n---', f'\ncover: {cover_path_normalized}\n---', 1)


def main():
    if len(sys.argv) < 2:
        print("用法: python auto_add_images.py <文章文件路径>")
        print("示例: python auto_add_images.py article.md")
        sys.exit(1)

    article_path = sys.argv[1]
    index_path = "C:/Users/anzib/gzhpublisher/config/image_embeddings_index.json"

    # 读取文章
    with open(article_path, 'r', encoding='utf-8') as f:
        article = f.read()

    print(f"正在为文章智能配图...")
    print(f"文章: {article_path}")
    print()

    # 提取frontmatter（保留，避免insert_images_into_article丢失）
    frontmatter, _ = extract_frontmatter(article)

    # 匹配图片
    matched_images = match_images_for_article(
        article,
        index_path,
        top_k=3,  # 每段最多匹配3张候选图片
        min_similarity=0.3  # 最低相似度阈值
    )

    # 插入图片（此步会丢失frontmatter，后面补回）
    article_with_images = insert_images_into_article(
        article,
        matched_images,
        max_images_per_article=5  # 全文最多插入5张图片
    )

    # 更新cover字段为相似度最高的图片，并补回frontmatter
    if frontmatter:
        if matched_images:
            top_image = max(matched_images, key=lambda x: x[2])
            top_image_path = top_image[0]
            updated_frontmatter = update_cover_in_frontmatter(frontmatter, top_image_path)
            print(f"\n✓ 已更新cover字段: {top_image[1]} (相似度: {top_image[2]:.3f})")
        else:
            updated_frontmatter = frontmatter
            print(f"\n- 无匹配图片，cover字段保持不变")
        article_with_images = updated_frontmatter + "\n\n" + article_with_images

    # 覆盖原文件
    with open(article_path, 'w', encoding='utf-8') as f:
        f.write(article_with_images)

    print(f"\n✓ 已更新文章: {article_path}")

if __name__ == "__main__":
    main()
