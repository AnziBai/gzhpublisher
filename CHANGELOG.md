# Changelog

## [Unreleased]

## [1.0.0] — 2026-04-23

### 项目初始化
- 从散落目录迁入：agents、skills、scripts、articles
- 统一路径：scripts 和 config 均在仓库内
- 新增 deploy.ps1（一键同步 agents/skills 到 ~/.claude/）

### 功能（继承自迁移前版本）
- kuanlun-geo-writer-enhanced Agent（2241行，含情绪分析、标题工程、开头钩子模块）
- kuanlun-article-auditor Agent（7项审核清单）
- 智能配图系统：embedding-3 召回 → GLM-5.1 精排
- 文章结尾模块（二维码 + FREE图 + 感谢语 + 斜体免责声明）
- 105张《概率的朋友》图库，4.3MB 向量索引

### Bug 修复
- 图片 alt text 由 description 改为完整文件名（去扩展名）
- 删除 agent 模板中冗余的"数据来源：第X章第X页"斜体行
- agent 模板图片语法从 `<img>` HTML 改为纯 Markdown `![]()`
