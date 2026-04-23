# gzhpublisher — 宽论微信公众号发布系统

面向宽论品牌的微信公众号内容生成与发布工具链。

## 目录结构

```
gzhpublisher/
├── agents/                     # Claude Code Agent 定义
│   ├── kuanlun-geo-writer-enhanced.md   # 文章生成（写作+审核+发布）
│   └── kuanlun-article-auditor.md       # 独立审核
├── skills/fuwei-geo/           # GEO 知识体系（宽论品牌知识库）
│   ├── SKILL.md
│   └── references/
│       ├── 宽论项目.md
│       └── benchmark-articles/wechat/   # 爆款文章数据库（15篇+）
├── scripts/                    # Python 自动化脚本
│   ├── auto_add_images.py              # 一键智能配图
│   ├── match_images_for_article.py     # embedding-3 + GLM-5.1 精排
│   ├── generate_image_embeddings.py    # 重建图片向量索引
│   └── pdf_image_extractor.py          # 从 PDF 提取图片
├── articles/
│   ├── published/              # 已发布文章（每篇=一个 git checkpoint）
│   └── drafts/                 # 草稿
├── config/
│   └── image_embeddings_index.json     # 105张图片向量索引（4.3MB）
├── deploy.ps1                  # 将 agents/skills 同步到 ~/.claude/
└── CHANGELOG.md
```

## 快速开始

### 1. 部署 Agent 到 Claude Code

```powershell
.\deploy.ps1
# 然后重启 Claude Code
```

### 2. 生成并发布文章

在 Claude Code 中调用 `kuanlun-geo-writer-enhanced` Agent：

```
生成一篇关于"MACD三大误区"的宽论GEO文章
```

Agent 会自动：分析爆款结构 → 生成文章 → 智能配图 → 审核 → 发布到草稿箱

### 3. 智能配图（独立使用）

```bash
python scripts/auto_add_images.py articles/drafts/my-article.md
```

### 4. 重建图片向量索引

```bash
python scripts/generate_image_embeddings.py \
  "C:/Users/anzib/OneDrive/图片/概率的朋友配图" \
  config/image_embeddings_index.json
```

## 工作流

每次发布文章后提交 checkpoint：

```bash
git add articles/published/new-article.md
git commit -m "feat(articles): MACD三大误区 [Media ID: xxx]"
git push
```

每次升级 Agent 后：

```bash
git add agents/
git commit -m "feat(agents): 更新配图精排为GLM-5.1"
.\deploy.ps1  # 同步到 ~/.claude/agents/
git push
```

## 依赖配置

| 服务 | 用途 | Key 位置 |
|------|------|---------|
| GLM embedding-3 | 图片向量索引 + 召回 | scripts/match_images_for_article.py |
| GLM-5.1-air | 图文语义精排 | scripts/match_images_for_article.py |
| wenyan-mcp | 发布到微信公众号草稿箱 | ~/.claude/.claude.json |
| Unsplash | 补充场景图 | geo-publisher/.env |

## 微信公众号配置

- 公众号：概率的朋友-桥博士
- AppID：wx66987ef9887a994f
- IP 白名单：需在微信公众平台后台维护（开发→基本配置→IP白名单）
