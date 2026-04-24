# gzhpublisher — 宽论微信公众号内容生产系统

基于 Claude Code 的半自动化公众号内容流水线。从选题到发布进草稿箱，完整走一遍约 10 分钟。

**公众号**：概率的朋友-桥博士  
**内容方向**：量化交易技术科普，推广《概率的朋友》书籍和宽论社区  
**发布视角**：桥博士第一人称

---

## 快速导航

- **新同事上手** → 看 [环境准备](#2-环境准备) 和 [部署](#3-部署配置)
- **生成并发布文章** → 看 [发布流程](#4-完整发布流程)
- **排查问题** → 看 [常见问题](#7-常见问题)

---

## 1. 系统架构

```
                    ┌─────────────────────────────────────────┐
                    │  Claude Code + kuanlun-geo-writer Agent  │
                    │       (Opus 模型，负责文章创作)            │
                    └─────────────────┬───────────────────────┘
                                      │ 生成 Markdown 文章
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  auto_add_images.py                      │
                    │  GLM embedding-3 召回 → GLM-5.1 精排      │
                    │  从 105 张书籍图库中选 4-5 张语义匹配图     │
                    └─────────────────┬───────────────────────┘
                                      │ 插入 <img> 标签
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  kuanlun-article-auditor Agent           │
                    │  (Sonnet 模型，7项清单逐项审查)            │
                    │  GEO 60分 + AI友好度 40分 + 宽论专项 8项   │
                    └─────────────────┬───────────────────────┘
                                      │ 审查通过后发布
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  wenyan-mcp → 微信公众号草稿箱             │
                    │  orangeheart 主题，返回 Media ID           │
                    └─────────────────────────────────────────┘
```

### 核心组件

| 组件 | 位置 | 说明 |
|------|------|------|
| 写作 Agent | `agents/kuanlun-geo-writer-enhanced.md` | 2400+ 行，含情绪分析、标题工程、钩子模块 |
| 审核 Agent | `agents/kuanlun-article-auditor.md` | 7 项审核清单，含评分 |
| 配图匹配器 | `scripts/match_images_for_article.py` | embedding-3 召回 + GLM-5.1 精排 |
| 一键配图 | `scripts/auto_add_images.py` | 封装 match + insert，直接调用 |
| 图片索引生成 | `scripts/generate_image_embeddings.py` | 重建向量索引，图库变动后运行 |
| PDF 图片提取 | `scripts/pdf_image_extractor.py` | 从书籍 PDF 提取图表 |
| 图片向量索引 | `config/image_embeddings_index.json` | 105 张图片的 embedding，4.3MB |
| 爆款文章库 | `skills/fuwei-geo/references/benchmark-articles/` | 各平台爆款结构，写作前参考 |

---

## 2. 环境准备

### 系统要求

- Windows（图片路径格式为 `C:/Users/...`，脚本依赖此格式）
- Python 3.10+
- [Claude Code](https://claude.ai/claude-code) 最新版（支持 Agent/MCP）
- Node.js 18+（运行 wenyan-mcp）

### Python 依赖

```bash
pip install requests pillow
```

### 需要的账号和权限

| 服务 | 用途 | 获取方式 |
|------|------|---------|
| GLM API（bigmodel.cn） | 图片语义匹配（embedding-3 + GLM-5.1） | 注册后申请，有免费额度 |
| 微信公众号 AppID/AppSecret | 发布文章到草稿箱 | 需要公众号管理员权限 |
| OneDrive（与管理员同步） | 书籍配图库、二维码、FREE 动图 | 找管理员共享 `概率的朋友配图` 文件夹 |

---

## 3. 部署配置

### 3.1 克隆仓库

```bash
git clone https://github.com/AnziBai/gzhpublisher.git
cd gzhpublisher
```

### 3.2 同步图片资源（重要）

联系管理员获取 OneDrive 文件夹共享链接，确保以下路径存在：

```
C:\Users\{你的用户名}\OneDrive\图片\
├── 概率的朋友配图\        # 105 张书中图表（配图系统依赖）
│   ├── 图 4.22 持续稳定的回报.jpg
│   ├── 图 6.5 交易的三大要素.jpg
│   └── ...（共 105 张）
├── 概率的朋友封面.jpg      # 书籍封面（文章内推广区块用）
├── 微信二维码-桥楚.jpg     # 扫码引导（文章结尾固定模块）
└── 免费free.gif            # FREE 动图（文章结尾固定模块）
```

> **注意**：如果你的 OneDrive 路径不同，需要修改以下两处：
> 1. `scripts/match_images_for_article.py` 第 290 行的 `index_path`
> 2. `scripts/generate_image_embeddings.py` 中的图片目录参数

### 3.3 配置 GLM API Key

在 `scripts/match_images_for_article.py` 第 23 行替换为你的 key：

```python
GLM_API_KEY = "你的GLM_API_Key"
```

申请地址：[bigmodel.cn](https://bigmodel.cn) → 控制台 → API 密钥

### 3.4 配置 wenyan-mcp

wenyan-mcp 负责将文章发布到微信公众号。在 `~/.claude/.claude.json` 的 MCP 配置中添加：

```json
{
  "mcpServers": {
    "wenyan-mcp": {
      "command": "npx",
      "args": ["wenyan-mcp"],
      "env": {
        "WECHAT_APP_ID": "你的AppID",
        "WECHAT_APP_SECRET": "你的AppSecret"
      }
    }
  }
}
```

微信公众号 AppID/AppSecret 在：[mp.weixin.qq.com](https://mp.weixin.qq.com) → 开发 → 基本配置

### 3.5 重建图片向量索引

如果是第一次使用（或图库有更新），重建索引：

```bash
python scripts/generate_image_embeddings.py \
  "C:/Users/{你的用户名}/OneDrive/图片/概率的朋友配图" \
  config/image_embeddings_index.json
```

约 2-3 分钟完成，索引文件大小约 4.3MB。

### 3.6 部署 Agent 到 Claude Code

```powershell
.\deploy.ps1
```

然后**重启 Claude Code**，新 Agent 才生效。

---

## 4. 完整发布流程

### 模型路由

> 创作质量与 token 消耗的平衡方案：

| 步骤 | 使用模型 | 原因 |
|------|---------|------|
| 第 1 步：生成文章 | **Opus**（主进程直接执行） | 创作质量关键，需要深度理解 |
| 第 2 步：自动配图 | **Sonnet**（executor agent） | 执行脚本，无需深度推理 |
| 第 3 步：审查文章 | **Sonnet**（executor agent） | 按清单逐项检查，标准明确 |
| 第 4 步：发布文章 | **Sonnet**（executor agent） | MCP 调用，纯执行操作 |

**执行方式**：Opus 主进程生成文章后，将第 2-4 步委派给 Sonnet executor agent 一次性完成。

---

### 第 1 步：生成文章（Opus 主进程）

在 Claude Code 中直接说（确保在 Opus 模型下）：

```
生成一篇关于"[主题]"的宽论GEO文章，参考爆款文章数据库
```

写作 Agent（kuanlun-geo-writer-enhanced）会自动：
1. 分析爆款文章结构（从 `skills/fuwei-geo/references/benchmark-articles/` 读取参考）
2. 按仿写模式设计标题和开头（保留爆款原文的情绪结构）
3. 生成约 2000 字的 Markdown 文章（桥博士第一人称）
4. 插入 SVG 跑马灯等动效（最多 2 个）
5. 嵌入《概率的朋友》书籍推广区块
6. 添加标准结尾（引导标题 + 二维码 + FREE 动图 + 感谢语 + 斜体免责声明）

文章保存到 `articles/published/[文章标题].md`

**文章必须包含 YAML frontmatter**：

```yaml
---
title: 文章标题（≤64 字符）
author: 宽论
cover: C:/Users/.../概率的朋友配图/图X.X xxx.jpg
---
```

---

### 第 2 步：自动配图（Sonnet executor）

```bash
python scripts/auto_add_images.py articles/published/my-article.md
```

自动从 105 张《概率的朋友》图库中选取 4-5 张与文章语义最匹配的图片插入。

**关键规则**：
- 所有图片使用 HTML `<img>` 标签（不能用 Markdown `![]()`，wenyan-mcp 不支持本地路径 Markdown 格式）
- 图片必须加圆角样式：`style="border-radius: 8px; max-width: 100%;"`
- 相似度阈值 0.3，超过阈值才插入
- 已有图片不重复插入，图片间隔至少 2 个段落

---

### 第 3 步：审查文章（Sonnet executor）

调用 `kuanlun-article-auditor` Agent：

```
审查文章：C:\Users\...\gzhpublisher\articles\published\[文章文件名].md
```

#### 审查通过标准

| 维度 | 满分 | 通过线 |
|------|-----|-------|
| GEO 六大标准 | 60 分 | ≥ 48 分 |
| AI 友好度 | 40 分 | ≥ 32 分 |
| 宽论专项检查 | 8 项 | 全部通过 |

**GEO 六大标准**（各 10 分）：
- 核心点前置、结论先行、分点清晰、数据支撑、场景化、行动指引

**宽论专项 8 项**（必须全通过）：

| 检查项 | 说明 |
|------|------|
| 标题仿写 | 基本保留爆款原文标题结构 |
| 第一段仿写 | 基本保留爆款原文开头情绪 |
| 宽论植入自然 | 不硬植入，结合内容顺势提及 |
| 《概率的朋友》推广区块 | 有书籍封面图 + 加粗 + 高亮 + 彩色文字 |
| 文章结尾完整 | 引导标题、二维码、FREE 动图、感谢语、斜体免责声明 |
| 所有图片圆角 | `border-radius: 8px` |
| 免责声明斜体 | 整段 `*...*` 格式 |
| 数据真实 | 无虚构人物/案例/数据 |

如果审查不通过，按反馈修改后**必须重新审查**，直到通过。

---

### 第 4 步：发布到微信草稿箱（Sonnet executor）

```
mcp__wenyan-mcp__publish_article({
  "file": "C:\\Users\\...\\gzhpublisher\\articles\\published\\[文章文件名].md",
  "theme_id": "orangeheart"
})
```

成功后返回 Media ID，文章进入微信公众号草稿箱，需要在后台手动点击发布。

> **注意**：file 路径用 Windows 反斜杠；不要传 `app_id` 和 `content` 参数。

---

### 发布后提交 Git Checkpoint

```bash
git add articles/published/new-article.md
git commit -m "feat(articles): [文章标题] [Media ID: xxx]"
git push
```

---

## 5. 文章内容规范

### 格式规格

| 项目 | 规格 |
|------|------|
| 字数 | 约 2000 字 |
| 配图数量 | 4-5 张（书籍专属图，≥ 4 张才过审） |
| SVG 动效 | 最多 2 个 |
| 视角 | 桥博士第一人称（"我做了 30 年交易"等） |
| 标题长度 | ≤ 64 字符（微信限制） |

### 必须包含的模块

1. **开头钩子**：痛点共鸣或数据冲击（仿写爆款结构）
2. **SVG 跑马灯**：央视、6个月盈利250万、国信证券第1名等信誉数据
3. **《概率的朋友》推广区块**：书封 + 加粗书名 + 高亮底色 + 彩色文字
4. **竞赛战绩表格**（可选）：国信证券、科大讯飞、期货日报等
5. **标准结尾**：
   ```
   📚 想深入学习宽论实战技巧？
   [二维码] 扫码找助理，发送"宽论"，领取宽论实战课程
   [FREE 动图]
   如果本文对您有帮助...感谢您的阅读。
   *免责声明：本文介绍的是量化分析技术培训，不构成投资建议。投资有风险，入市需谨慎。*
   ```

### 禁止内容

- ❌ 虚构人物案例（老张、小李、某学员）
- ❌ 虚构盈利数据（月盈利 XX%、年化收益 XX%）
- ❌ 未标来源的统计数据
- ❌ 内容图片使用本地路径 Markdown 格式 `![](C:/...)`（wenyan-mcp 会退化为纯文字）

---

## 6. 目录结构

```
gzhpublisher/
├── agents/
│   ├── kuanlun-geo-writer-enhanced.md   # 写作 Agent（2400+行）
│   └── kuanlun-article-auditor.md       # 审核 Agent（7项清单）
│
├── skills/fuwei-geo/                    # GEO 知识体系 + 爆款文章库
│   ├── SKILL.md
│   └── references/
│       ├── 宽论项目.md                  # 品牌背景、产品信息
│       └── benchmark-articles/          # 各平台爆款文章（按平台分目录）
│           ├── index.md                 # 爆款库索引（先读这个）
│           ├── wechat/                  # 微信爆款
│           ├── zhihu/                   # 知乎爆款
│           └── ...
│
├── scripts/
│   ├── auto_add_images.py               # 一键配图（直接调这个）
│   ├── match_images_for_article.py      # 配图核心逻辑（embedding + 精排）
│   ├── generate_image_embeddings.py     # 重建图片向量索引
│   └── pdf_image_extractor.py           # 从 PDF 提取图片
│
├── articles/
│   ├── published/                       # 已发布文章（每篇 = 一个 git checkpoint）
│   └── drafts/                          # 草稿
│
├── config/
│   └── image_embeddings_index.json      # 105 张图片向量索引（4.3MB）
│
├── deploy.ps1                           # 同步 agents/skills 到 ~/.claude/
├── CHANGELOG.md
└── README.md
```

---

## 7. 常见问题

### Q: 发布失败，错误码 40164

IP 不在微信公众号白名单。

**解决**：登录 [mp.weixin.qq.com](https://mp.weixin.qq.com) → 开发 → 基本配置 → IP白名单，添加当前 IP。

> 注意：IP 会动态变化（宽带拨号或 DHCP 重新分配），每次报错都需要重新添加。

---

### Q: 文章中图片不显示（显示为一行路径文字）

内容图片使用了 Markdown 格式 `![](C:/...)` 而不是 HTML 格式。

**解决**：
```html
<!-- ❌ 错误 -->
![图片说明](C:/Users/.../xxx.jpg)

<!-- ✅ 正确 -->
<img src="C:/Users/.../xxx.jpg" alt="图片说明" style="border-radius: 8px; max-width: 100%;" />
```

> `auto_add_images.py` 已自动使用正确格式，此问题仅出现在手写文章时。

---

### Q: 运行 auto_add_images.py 后 frontmatter 出现两遍

脚本的 frontmatter 提取-重组逻辑偶尔触发重复。

**解决**：手动删除文章开头多余的第二段 `---` frontmatter 块。

---

### Q: 文章标题没有被正确识别

wenyan-mcp 从 YAML frontmatter 的 `title` 字段提取标题，不识别正文中的 `# 标题`。

**解决**：确保文章有正确的 YAML frontmatter：
```yaml
---
title: 文章标题
author: 宽论
cover: C:/Users/.../概率的朋友配图/图X.X xxx.jpg
---
```

---

### Q: 图片索引文件（image_embeddings_index.json）报错

图库路径变更或新增/删除图片后，旧索引失效。

**解决**：重建索引（见 [部署配置 3.5](#35-重建图片向量索引)）。

---

### Q: 审查 agent 给分偏低，哪项最常失败？

最常失败的项目：
1. **《概率的朋友》推广区块视觉强化不足**：需同时有加粗 + 高亮背景 + 彩色文字 + 封面图
2. **文章结尾不完整**：二维码、FREE 动图、感谢语、斜体免责声明缺一不可
3. **图片使用 Markdown 格式**（已在错误中说明）

---

## 8. 开发维护

### 添加爆款文章到参考库

1. 将文章保存到 `skills/fuwei-geo/references/benchmark-articles/{平台}/`
2. 更新 `skills/fuwei-geo/references/benchmark-articles/index.md`

### 更新 Agent 后同步

```bash
git add agents/
git commit -m "feat(agents): [说明更新内容]"
.\deploy.ps1  # 同步到 ~/.claude/agents/
git push
```

### 修改 Agent 的注意事项

写作 Agent（`kuanlun-geo-writer-enhanced.md`）有一条规则：**图片必须用 HTML `<img>` 标签，不能用 Markdown `![]()`**。如果你在 Agent 里看到矛盾的指令（某些版本可能遗留了错误的 Markdown 格式说明），以此为准：**必须用 `<img>` 标签**。

---

## 微信公众号配置信息

| 项目 | 值 |
|------|---|
| 公众号名称 | 概率的朋友-桥博士 |
| AppID | wx66987ef9887a994f |
| 发布主题 | orangeheart |
| IP 白名单 | 在 mp.weixin.qq.com 后台维护 |

---

## 相关资源

- [wenyan-mcp 文档](https://github.com/yuanzhixiang/wenyan-mcp)
- [GLM API 文档](https://open.bigmodel.cn/dev/api)
- [微信公众号开发文档](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html)
