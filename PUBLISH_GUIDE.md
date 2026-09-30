# GitHub 发布指南

## 项目信息
- **项目名称**: docx_to_md
- **版本**: v1.0.0
- **作者**: 倪啸庭
- **所属单位**: 齐齐哈尔医学院、哈尔滨医科大学附属第一医院
- **开源协议**: MIT License

## 📦 项目已完成
✅ 所有文件已创建并提交到Git
✅ 版本标签 v1.0.0 已创建
✅ README支持中英双语
✅ 可执行文件已打包（14MB）

---

## 🚀 发布步骤

### 步骤1：在GitHub上创建仓库

1. 访问 https://github.com/new
2. 填写以下信息：
   - **Repository name**: `docx_to_md`
   - **Description**: `批量将DOCX文件转换为Markdown文件的工具 / Batch convert DOCX files to Markdown`
   - **Visibility**: 选择 `Public`（公开）
   - **不要勾选** "Add a README file"
   - **不要勾选** "Add .gitignore"
   - **不要选择** License（我们已经有了）
3. 点击 `Create repository`

### 步骤2：推送代码到GitHub

打开命令行（Git Bash或Windows Terminal），执行以下命令：

```bash
cd /d/Github/docx_to_md

# 添加远程仓库（将 YOUR_USERNAME 替换为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/docx_to_md.git

# 推送代码
git push -u origin master

# 推送标签
git push origin v1.0.0
```

如果提示需要登录，按照提示输入GitHub账号密码或使用Personal Access Token。

### 步骤3：创建Release并上传exe文件

1. 在GitHub仓库页面，点击右侧的 `Releases`（或访问 `https://github.com/YOUR_USERNAME/docx_to_md/releases`）
2. 点击 `Create a new release`
3. 填写Release信息：

**Choose a tag**: 选择 `v1.0.0`

**Release title**: `v1.0.0 - Initial Release / 首次发布`

**Description**（复制以下内容）:
```markdown
## 首次发布 / Initial Release 🎉

### 功能特点 / Features
- ✅ 批量转换.docx文件为.md文件 / Batch convert .docx files to .md files
- ✅ 支持中英文混合文档 / Support mixed Chinese-English documents
- ✅ 支持标题、段落、表格、加粗、斜体等格式 / Support headings, paragraphs, tables, bold, italic formats
- ✅ 单文件exe，无需安装Python环境 / Single file exe, no Python installation required
- ✅ 自动跳过临时文件 / Automatically skip temporary files
- ✅ 显示详细的转换进度和统计 / Display detailed conversion progress and statistics

### 使用方法 / Usage
1. 下载 `docx_to_md_converter.exe` / Download `docx_to_md_converter.exe`
2. 将exe放到包含docx文件的文件夹 / Place exe in folder with docx files
3. 双击运行 / Double-click to run
4. 查看生成的.md文件 / Check generated .md files

### 系统要求 / System Requirements
- Windows 7/8/10/11
- 无需Python环境 / No Python required

### 作者 / Author
倪啸庭 / Ni Xiaoting
- 齐齐哈尔医学院 / Qiqihar Medical University
- 哈尔滨医科大学附属第一医院 / The First Affiliated Hospital of Harbin Medical University
```

4. **上传文件**：点击 "Attach binaries by dropping them here or selecting them"
   - 将 `D:\Github\docx_to_md\releases\docx_to_md_converter.exe` 拖拽到文件区域

5. 确认无误后，点击 `Publish release`

### 步骤4：完善仓库信息

1. 在仓库主页，点击右侧的 `About` 旁边的齿轮图标 ⚙️
2. 填写以下信息：
   - **Description**: `批量将DOCX文件转换为Markdown文件的工具 / Batch convert DOCX files to Markdown`
   - **Website**: 留空
   - **Topics**: 添加标签（可选）：
     - `docx`
     - `markdown`
     - `converter`
     - `batch-processing`
     - `python`
     - `windows`
     - `chinese`
3. 勾选 `Releases`
4. 点击 `Save changes`

---

## ✅ 发布完成检查清单

完成以上步骤后，确认以下内容：

- [ ] 仓库已创建并设为Public
- [ ] 代码已成功推送到master分支
- [ ] 标签v1.0.0已推送
- [ ] Release已创建并上传exe文件
- [ ] README中英双语显示正常
- [ ] About部分信息已填写

---

## 📝 后续操作（可选）

### 1. 更新README中的链接
将README.md中的所有 `YOUR_USERNAME` 替换为你的实际GitHub用户名：
```bash
cd /d/Github/docx_to_md
# 手动编辑README.md，替换YOUR_USERNAME
git add README.md
git commit -m "Update GitHub username in README"
git push
```

### 2. 添加GitHub徽章
你可以在README中添加更多徽章，例如：
- ![Downloads](https://img.shields.io/github/downloads/YOUR_USERNAME/docx_to_md/total)
- ![Stars](https://img.shields.io/github/stars/YOUR_USERNAME/docx_to_md)

### 3. 宣传你的项目
- 在相关社区分享
- 添加到awesome-lists
- 在社交媒体上推广

---

## 🔗 最终链接

发布完成后，你的项目将在以下位置：

- **仓库**: `https://github.com/YOUR_USERNAME/docx_to_md`
- **Release**: `https://github.com/YOUR_USERNAME/docx_to_md/releases`
- **下载exe**: `https://github.com/YOUR_USERNAME/docx_to_md/releases/download/v1.0.0/docx_to_md_converter.exe`

---

## 💡 提示

- 推送代码可能需要GitHub Personal Access Token（如果启用了2FA）
- exe文件大小为14MB，上传可能需要几分钟
- 确保网络连接稳定

**祝发布顺利！🎉**
