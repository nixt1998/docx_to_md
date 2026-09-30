# 如何推送到GitHub

项目已准备就绪！按照以下步骤将项目推送到GitHub：

## 步骤1：在GitHub上创建仓库

1. 访问 https://github.com/new
2. 仓库名称填写：`docx_to_md`
3. 描述填写：`批量将DOCX文件转换为Markdown文件的工具`
4. 选择 `Public`（公开仓库）
5. **不要**勾选 "Add a README file"（我们已经有了）
6. **不要**勾选 "Add .gitignore"（我们已经有了）
7. License 选择 `MIT License`（或跳过，我们已经有了）
8. 点击 `Create repository`

## 步骤2：关联远程仓库并推送

在命令行中执行以下命令（将 YOUR_USERNAME 替换为你的GitHub用户名）：

```bash
cd /d/Github/docx_to_md

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/docx_to_md.git

# 推送代码和标签
git push -u origin master
git push origin v1.0.0
```

## 步骤3：创建Release

1. 在GitHub仓库页面，点击右侧的 `Releases`
2. 点击 `Create a new release`
3. 选择标签：`v1.0.0`
4. Release标题：`v1.0.0 - Initial Release`
5. 描述可以填写：
   ```
   ## 首次发布 🎉
   
   ### 功能特点
   - ✅ 批量转换.docx文件为.md文件
   - ✅ 支持标题、段落、表格、加粗、斜体等格式
   - ✅ 单文件exe，无需安装Python环境
   - ✅ 自动跳过临时文件
   - ✅ 显示详细的转换进度和统计
   
   ### 下载
   下载 `docx_to_md_converter.exe` 即可使用
   ```
6. 上传文件：将 `releases/docx_to_md_converter.exe` 拖拽到文件区域
7. 点击 `Publish release`

## 完成！

你的项目现在已经开源到GitHub上了！🎉

仓库地址将是：`https://github.com/YOUR_USERNAME/docx_to_md`
