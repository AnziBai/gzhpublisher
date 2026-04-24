# Changelog

## [Unreleased]

## [1.1.0] — 2026-04-24

### 流程优化
- 模型路由：第1步生成改用 Opus，第2-4步委派 Sonnet executor agent，节省 token
- 文章篇幅调整为 2000 字左右，配图 4-5 张（从 3000-4000 字 / 5-8 张降档）
- `max_images_per_article` 调整为 5

### Bug 修复
- `match_images_for_article.py`：`insert_images_into_article` 改为操作 `all_blocks`（含所有原始块），
  修复之前重建文章时丢失 `##` 标题和 `---` 分隔线的问题
- `kuanlun-article-auditor.md`：新增图片 URL 格式检查（内容图片必须为 Web URL 或 `<img>` 标签）
  和发布主题检查（默认 orangeheart）

### 已发布文章
- MACD背离——高手藏着不说的技巧（Media ID: `_D93UH1J7L1p5g5_Coy3GT6a24tibsMxeI9qzgdytAZFDggOGmFFrMTbg_rjFrit`）
- 7种K线形态的量化真相（Media ID: `_D93UH1J7L1p5g5_Coy3Getki33pzacLbzKA3vDxb754N8o2FixBUUgX3CDj33Lp`）
- 90%散户亏钱的真相：你一直在和概率作对（Media ID: `_D93UH1J7L1p5g5_Coy3GdLq5MycbgrechwlclH2y5y9zU_LgPrQi2kLq4H_rAQW`）

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
