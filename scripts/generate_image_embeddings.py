#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片向量索引生成器
功能：扫描图库，为每张图片的文件名生成embedding向量，保存为JSON索引
"""

import sys
import os
import json
import requests
from pathlib import Path

# Windows 控制台编码
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# GLM API配置
GLM_API_KEY = "f9761e349d4947b4b54ac77b51da78c5.kGF1NoHb0jkaASUm"
GLM_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"

def get_embedding(text: str) -> list:
    """
    调用GLM Embedding API获取文本向量
    """
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

    # 检查响应
    if response.status_code != 200:
        raise ValueError(f"GLM API错误 ({response.status_code}): {response.text}")

    data = response.json()

    if "data" not in data or len(data["data"]) == 0:
        raise ValueError("GLM API返回空向量")

    return data["data"][0]["embedding"]

def scan_image_library(image_dir: str) -> dict:
    """
    扫描图库，为每张图片生成向量索引

    返回格式：
    {
        "图 1.3 海龟交易法则与 MACD 模型的权益图.jpg": {
            "path": "C:/Users/anzib/OneDrive/图片/概率的朋友配图/图 1.3 海龟交易法则与 MACD 模型的权益图.jpg",
            "filename": "图 1.3 海龟交易法则与 MACD 模型的权益图.jpg",
            "description": "海龟交易法则与 MACD 模型的权益图",
            "embedding": [0.123, 0.456, ...]
        }
    }
    """
    image_dir = Path(image_dir)
    index = {}

    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

    # 扫描所有图片
    image_files = [f for f in image_dir.iterdir()
                   if f.is_file() and f.suffix.lower() in image_extensions]

    print(f"找到 {len(image_files)} 张图片")

    for i, img_file in enumerate(image_files, 1):
        filename = img_file.name

        # 提取描述（去掉"图 X.X "前缀和扩展名）
        description = filename
        if description.startswith("图 "):
            # 去掉"图 1.3 "这样的前缀
            parts = description.split(" ", 2)
            if len(parts) >= 3:
                description = parts[2]
        # 去掉扩展名
        description = Path(description).stem

        print(f"[{i}/{len(image_files)}] 处理: {filename}")
        print(f"  描述: {description}")

        try:
            # 生成embedding（使用描述文字）
            embedding = get_embedding(description)

            index[filename] = {
                "path": str(img_file.absolute()).replace("\\", "/"),
                "filename": filename,
                "description": description,
                "embedding": embedding
            }

            print(f"  ✓ 向量维度: {len(embedding)}")

        except Exception as e:
            print(f"  ✗ 错误: {e}")
            continue

    return index

def main():
    # 从环境变量或命令行参数获取配置
    _repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_repo_root, "assets", "概率的朋友配图")
    output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(_repo_root, "config", "image_embeddings_index.json")

    print(f"图库目录: {image_dir}")
    print(f"输出文件: {output_file}")
    print()

    # 生成索引
    index = scan_image_library(image_dir)

    # 保存为JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print()
    print(f"✓ 索引已保存: {output_file}")
    print(f"✓ 共索引 {len(index)} 张图片")

if __name__ == "__main__":
    main()
