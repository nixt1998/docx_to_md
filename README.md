# DOCX to Markdown Batch Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/YOUR_USERNAME/docx_to_md/releases)

**English** | [简体中文](README_CH.md)

A simple and efficient batch conversion tool that converts all Word documents (.docx) in a folder to Markdown files (.md).

**Supports documents with mixed Chinese and English content**, perfectly handling Chinese characters!

## ✨ Features

- 🚀 Batch convert all .docx files in the current directory
- 🌍 **Full support for mixed Chinese-English documents** (UTF-8 encoding)
- 📝 Preserve original filenames, only change extensions
- 🎨 Support multiple formats:
  - Headings (Heading 1-6)
  - Paragraph text
  - Bold and italic text
  - Tables (automatically converted to markdown table format)
  - Mixed formatting (bold + italic)
- ⚡ Automatically skip temporary files (files starting with ~$)
- 📊 Display conversion progress and result statistics
- 💾 Single file exe, no Python environment required

## 📦 Download & Installation

### Option 1: Direct exe download (Recommended)

1. Go to the [Releases](https://github.com/YOUR_USERNAME/docx_to_md/releases) page
2. Download the latest version of `docx_to_md_converter.exe`
3. Place the exe file in the folder containing docx files
4. Double-click to run

### Option 2: Use Python source code

If you have Python 3.8+ installed:

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/docx_to_md.git
cd docx_to_md

# Install dependencies
pip install -r requirements.txt

# Run script
python docx_to_md_converter.py
```

## 🎯 Usage

### Using the exe file

1. Copy `docx_to_md_converter.exe` to the folder containing docx files
2. Double-click to run `docx_to_md_converter.exe`
3. The program will automatically scan and convert all docx files in the same directory
4. After conversion, view the statistics and press Enter to exit

### Example Output

```
============================================================
DOCX Batch to MD Tool
============================================================
Working Directory: C:\Users\Documents

Found 3 docx files:
  - research_report.docx
  - meeting_notes.docx
  - project_doc.docx

Converting: research_report.docx -> research_report.md ... ✓ Success
Converting: meeting_notes.docx -> meeting_notes.md ... ✓ Success
Converting: project_doc.docx -> project_doc.md ... ✓ Success

============================================================
Conversion complete! Success: 3, Failed: 0
============================================================
```

## 🔧 Build exe from source

If you need to build the exe file yourself:

```bash
# Install dependencies
pip install -r requirements.txt

# Package as single exe file
pyinstaller --onefile --console --name docx_to_md_converter docx_to_md_converter.py
```

After packaging, the exe file will be in the `dist` directory.

## 📋 Supported Formats

| Format | Support Status |
|--------|---------------|
| Headings (Heading 1-6) | ✅ |
| Paragraph text | ✅ |
| Bold text | ✅ |
| Italic text | ✅ |
| Bold + Italic | ✅ |
| Tables | ✅ |
| Chinese characters | ✅ |
| English characters | ✅ |
| Mixed Chinese-English | ✅ |
| Images | ❌ |
| Hyperlinks | ⚠️ Partial support |

## 📝 Notes

- ✅ The program will not delete or modify original .docx files
- ⚠️ If a .md file with the same name exists, it will be overwritten
- 📁 Conversion scope: All .docx files in the exe directory only
- 🚫 Automatically skip temporary files (starting with ~$)
- 🌍 Uses UTF-8 encoding, perfect support for Chinese

## 🖥️ System Requirements

- **Operating System**: Windows 7/8/10/11
- **Python Version**: 3.8+ (only required for source code execution)
- **Dependencies**:
  - python-docx >= 1.1.2
  - pyinstaller >= 6.15.0 (only required for packaging)

## 👨‍💻 Author

**Ni Xiaoting**
- Qiqihar Medical University
- The First Affiliated Hospital of Harbin Medical University

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing

Issues and Pull Requests are welcome!

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📮 Contact

For questions or suggestions, please:

- Submit an [Issue](https://github.com/YOUR_USERNAME/docx_to_md/issues)

## 🙏 Acknowledgments

- [python-docx](https://python-docx.readthedocs.io/) - Python library for processing Word documents
- [PyInstaller](https://www.pyinstaller.org/) - Tool for packaging Python programs

---

⭐ If this project helps you, please give it a Star!
