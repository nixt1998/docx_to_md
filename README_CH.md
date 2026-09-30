# DOCX to Markdown 批量转换工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/YOUR_USERNAME/docx_to_md/releases)

[English](README.md) | **简体中文**

一个简单高效的批量转换工具，可以将文件夹中的所有Word文档(.docx)转换为Markdown文件(.md)。

**支持中英文混合文档**，完美处理中文字符！

## ✨ 功能特点

- 🚀 批量转换当前目录下的所有.docx文件
- 🌍 **完全支持中英文混合文档**（UTF-8编码）
- 📝 保留原文件名，仅更改扩展名
- 🎨 支持多种格式：
  - 标题（Heading 1-6）
  - 段落文本
  - 加粗、斜体文本
  - 表格（自动转为markdown表格格式）
  - 混合格式（加粗+斜体）
- ⚡ 自动跳过临时文件（~$开头的文件）
- 📊 显示转换进度和结果统计
- 💾 单文件exe，无需安装Python环境

## 📦 下载安装

### 方式一：直接下载exe文件（推荐）

1. 前往 [Releases](https://github.com/YOUR_USERNAME/docx_to_md/releases) 页面
2. 下载最新版本的 `docx_to_md_converter.exe`
3. 将exe文件放到包含docx文件的文件夹中
4. 双击运行即可

### 方式二：使用Python源码

如果您已安装Python 3.8+环境：

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/docx_to_md.git
cd docx_to_md

# 安装依赖
pip install -r requirements.txt

# 运行脚本
python docx_to_md_converter.py
```

## 🎯 使用方法

### 使用exe文件

1. 将 `docx_to_md_converter.exe` 复制到包含docx文件的文件夹中
2. 双击运行 `docx_to_md_converter.exe`
3. 程序会自动扫描并转换同目录下的所有docx文件
4. 转换完成后，查看统计结果，按回车键退出

### 运行示例

```
============================================================
DOCX批量转MD工具
============================================================
工作目录: C:\Users\Documents

找到 3 个docx文件：
  - 研究报告.docx
  - meeting_notes.docx
  - 项目文档.docx

正在转换: 研究报告.docx -> 研究报告.md ... ✓ 成功
正在转换: meeting_notes.docx -> meeting_notes.md ... ✓ 成功
正在转换: 项目文档.docx -> 项目文档.md ... ✓ 成功

============================================================
转换完成！成功: 3, 失败: 0
============================================================
```

## 🔧 从源码打包exe

如果需要自行打包exe文件：

```bash
# 安装依赖
pip install -r requirements.txt

# 打包为单个exe文件
pyinstaller --onefile --console --name docx_to_md_converter docx_to_md_converter.py
```

打包完成后，exe文件位于 `dist` 目录中。

## 📋 支持的格式

| 格式 | 支持状态 |
|------|---------|
| 标题（Heading 1-6） | ✅ |
| 段落文本 | ✅ |
| 加粗文本 | ✅ |
| 斜体文本 | ✅ |
| 加粗+斜体 | ✅ |
| 表格 | ✅ |
| 中文字符 | ✅ |
| 英文字符 | ✅ |
| 中英混合 | ✅ |
| 图片 | ❌ |
| 超链接 | ⚠️ 部分支持 |

## 📝 注意事项

- ✅ 程序不会删除或修改原始.docx文件
- ⚠️ 如果已存在同名.md文件，将被覆盖
- 📁 转换范围：仅exe所在目录的所有.docx文件
- 🚫 自动跳过临时文件（~$开头）
- 🌍 使用UTF-8编码，完美支持中文

## 🖥️ 系统要求

- **操作系统**：Windows 7/8/10/11
- **Python版本**：3.8+ （仅源码运行时需要）
- **依赖包**：
  - python-docx >= 1.1.2
  - pyinstaller >= 6.15.0 （仅打包时需要）

## 👨‍💻 作者信息

**倪啸庭**
- 齐齐哈尔医学院
- 哈尔滨医科大学附属第一医院

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📮 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 [Issue](https://github.com/YOUR_USERNAME/docx_to_md/issues)

## 🙏 致谢

- [python-docx](https://python-docx.readthedocs.io/) - 用于处理Word文档的Python库
- [PyInstaller](https://www.pyinstaller.org/) - 用于打包Python程序的工具

---

⭐ 如果这个项目对您有帮助，请给它一个Star！
