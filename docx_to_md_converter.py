#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DOCX批量转MD工具
将当前目录下的所有.docx文件转换为.md文件
"""

import os
import sys
from pathlib import Path
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph


def get_document_elements(doc):
    """获取文档中的所有元素（段落和表格），保持原始顺序"""
    elements = []
    for element in doc.element.body:
        if isinstance(element, CT_P):
            elements.append(('paragraph', Paragraph(element, doc)))
        elif isinstance(element, CT_Tbl):
            elements.append(('table', Table(element, doc)))
    return elements


def paragraph_to_markdown(paragraph):
    """将段落转换为markdown格式"""
    text = paragraph.text.strip()
    if not text:
        return ""

    # 处理标题
    style = paragraph.style.name.lower()
    if 'heading 1' in style or 'title' in style:
        return f"# {text}\n"
    elif 'heading 2' in style:
        return f"## {text}\n"
    elif 'heading 3' in style:
        return f"### {text}\n"
    elif 'heading 4' in style:
        return f"#### {text}\n"
    elif 'heading 5' in style:
        return f"##### {text}\n"
    elif 'heading 6' in style:
        return f"###### {text}\n"

    # 处理加粗和斜体
    md_text = ""
    for run in paragraph.runs:
        run_text = run.text
        if run.bold and run.italic:
            run_text = f"***{run_text}***"
        elif run.bold:
            run_text = f"**{run_text}**"
        elif run.italic:
            run_text = f"*{run_text}*"
        md_text += run_text

    return md_text + "\n"


def table_to_markdown(table):
    """将表格转换为markdown格式"""
    if not table.rows:
        return ""

    md_lines = []

    # 处理表头
    header_cells = [cell.text.strip() for cell in table.rows[0].cells]
    md_lines.append("| " + " | ".join(header_cells) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")

    # 处理数据行
    for row in table.rows[1:]:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        md_lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(md_lines) + "\n"


def convert_docx_to_md(docx_path, md_path):
    """将单个docx文件转换为md文件"""
    try:
        doc = Document(docx_path)
        markdown_content = []

        # 获取所有元素并转换
        elements = get_document_elements(doc)
        for element_type, element in elements:
            if element_type == 'paragraph':
                md_text = paragraph_to_markdown(element)
                if md_text:
                    markdown_content.append(md_text)
            elif element_type == 'table':
                md_table = table_to_markdown(element)
                if md_table:
                    markdown_content.append("\n" + md_table + "\n")

        # 写入md文件
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))

        return True, None
    except Exception as e:
        return False, str(e)


def main():
    """主函数：批量转换当前目录下的所有docx文件"""
    # 获取脚本所在目录
    if getattr(sys, 'frozen', False):
        # 如果是打包后的exe
        current_dir = Path(sys.executable).parent
    else:
        # 如果是脚本运行
        current_dir = Path(__file__).parent

    print("=" * 60)
    print("DOCX批量转MD工具")
    print("=" * 60)
    print(f"工作目录: {current_dir}")
    print()

    # 查找所有docx文件
    docx_files = list(current_dir.glob("*.docx"))
    # 过滤掉临时文件（以~$开头的文件）
    docx_files = [f for f in docx_files if not f.name.startswith('~$')]

    if not docx_files:
        print("未找到任何.docx文件")
        input("\n按回车键退出...")
        return

    print(f"找到 {len(docx_files)} 个docx文件：")
    for f in docx_files:
        print(f"  - {f.name}")
    print()

    # 批量转换
    success_count = 0
    fail_count = 0

    for docx_file in docx_files:
        md_file = docx_file.with_suffix('.md')
        print(f"正在转换: {docx_file.name} -> {md_file.name} ... ", end='')

        success, error = convert_docx_to_md(docx_file, md_file)

        if success:
            print("✓ 成功")
            success_count += 1
        else:
            print(f"✗ 失败")
            print(f"  错误信息: {error}")
            fail_count += 1

    print()
    print("=" * 60)
    print(f"转换完成！成功: {success_count}, 失败: {fail_count}")
    print("=" * 60)

    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
