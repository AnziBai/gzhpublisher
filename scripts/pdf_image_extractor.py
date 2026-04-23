#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF 图片提取工具
用途：从 PDF 文件中提取指定页面的图片
作者：Claude Code
日期：2026-04-23
"""

import sys
import os
from pathlib import Path
import argparse
import fitz  # PyMuPDF

# 设置 Windows 控制台编码
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def extract_images_from_pdf(pdf_path, pages, output_dir, prefix=""):
    """
    从 PDF 中提取图片

    Args:
        pdf_path: PDF 文件路径
        pages: 页码列表，如 [1, 2, 3] 或 "1-3" 或 "all"
        output_dir: 输出目录
        prefix: 文件名前缀

    Returns:
        提取的图片文件路径列表
    """
    # 确保输出目录存在
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 打开 PDF
    pdf_document = fitz.open(pdf_path)
    total_pages = len(pdf_document)

    # 解析页码
    if pages == "all":
        page_list = range(total_pages)
    elif isinstance(pages, str) and "-" in pages:
        start, end = pages.split("-")
        page_list = range(int(start) - 1, int(end))  # PDF 页码从 1 开始，fitz 从 0 开始
    elif isinstance(pages, list):
        page_list = [p - 1 for p in pages]  # 转换为 0-based index
    else:
        page_list = [int(pages) - 1]

    extracted_files = []
    image_count = 0

    print(f"📄 PDF: {Path(pdf_path).name}")
    print(f"📊 总页数: {total_pages}")
    print(f"🎯 提取页面: {pages}")
    print(f"📁 输出目录: {output_dir}")
    print("-" * 60)

    for page_num in page_list:
        if page_num >= total_pages:
            print(f"⚠️  页码 {page_num + 1} 超出范围，跳过")
            continue

        page = pdf_document[page_num]
        image_list = page.get_images()

        print(f"\n📖 第 {page_num + 1} 页: 找到 {len(image_list)} 张图片")

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # 生成文件名
            if prefix:
                filename = f"{prefix}_第{page_num + 1}页_图{img_index + 1}.{image_ext}"
            else:
                filename = f"第{page_num + 1}页_图{img_index + 1}.{image_ext}"

            output_path = output_dir / filename

            # 保存图片
            with open(output_path, "wb") as img_file:
                img_file.write(image_bytes)

            extracted_files.append(str(output_path))
            image_count += 1

            # 显示图片信息
            size_kb = len(image_bytes) / 1024
            print(f"  ✅ {filename} ({size_kb:.1f} KB)")

    pdf_document.close()

    print("-" * 60)
    print(f"🎉 完成！共提取 {image_count} 张图片")

    return extracted_files


def main():
    parser = argparse.ArgumentParser(
        description="从 PDF 中提取图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法：
  # 提取第 26-27 页的图片
  python pdf_image_extractor.py input.pdf -p 26-27 -o output_dir

  # 提取所有页面的图片
  python pdf_image_extractor.py input.pdf -p all -o output_dir

  # 提取特定页面并添加前缀
  python pdf_image_extractor.py input.pdf -p 26-27 -o output_dir --prefix MACD回测图
        """
    )

    parser.add_argument("pdf_path", help="PDF 文件路径")
    parser.add_argument("-p", "--pages", default="all",
                        help="页码范围，如 '26-27' 或 'all' (默认: all)")
    parser.add_argument("-o", "--output", required=True,
                        help="输出目录")
    parser.add_argument("--prefix", default="",
                        help="文件名前缀 (可选)")

    args = parser.parse_args()

    # 检查 PDF 文件是否存在
    if not os.path.exists(args.pdf_path):
        print(f"❌ 错误：PDF 文件不存在: {args.pdf_path}")
        sys.exit(1)

    try:
        extracted_files = extract_images_from_pdf(
            args.pdf_path,
            args.pages,
            args.output,
            args.prefix
        )

        if extracted_files:
            print(f"\n📋 提取的文件列表：")
            for f in extracted_files:
                print(f"  - {f}")
        else:
            print("\n⚠️  没有提取到任何图片")

    except Exception as e:
        print(f"\n❌ 错误：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
