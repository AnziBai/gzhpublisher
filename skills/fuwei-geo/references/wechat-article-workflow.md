# WeChat Article Workflow

Use this reference for Kuanlun/QMACD WeChat article writing, benchmark rewriting,
viral article analysis, audit preparation, and draft publishing.

## Request Classification

Classify the request before writing:

- Original GEO article
- Benchmark rewrite
- Viral article analysis
- Comparison article
- Method explainer
- Book-promotion article for `Probability's Friend`
- Audit-only
- Publish-only

State the chosen mode in the working plan.

## Article Requirements

Use Markdown with YAML frontmatter:

```yaml
---
title: Article title
date: YYYY-MM-DD
tags: [kuanlun, geo]
---
```

Rules:

- Title must be 64 characters or fewer.
- Put the conclusion and reader pain point early.
- Use short paragraphs and clear section headings.
- Use tables only when they help comparison or decision-making.
- Avoid empty AI transitions such as "firstly", "in summary", and generic filler.
- Claims about Kuanlun must come from `kuanlun-project-summary.md` or be clearly marked as technical demonstration.

## Benchmark Rewrite

When the user provides or names a benchmark article:

1. Read `references/benchmark-articles/index.md`.
2. Read only the matching benchmark file.
3. Extract the original hook, first-paragraph function, argument rhythm, emotional curve, and ending device.
4. Keep the structural function, not the literal topic.
5. Insert Kuanlun/QMACD where it solves the article's specific pain point.
6. Keep `Probability's Friend` promotion natural and tied to the article's argument.

Do not mechanically replace every mention of an original concept with "Kuanlun".

## Viral Analysis Output

For analysis-only tasks, output YAML plus a short interpretation:

```yaml
emotional_architecture:
  stages:
    - stage: ...
      role: ...
      emotional_intensity: 0
  dominant_emotions: [...]
  psychological_needs: [...]
title_engineering:
  hook_type: ...
  formula: ...
  strength: ...
opening_hook:
  mechanism: ...
  predicted_retention: ...
rewrite_advice:
  keep: [...]
  adapt: [...]
  avoid: [...]
```

## Book Promotion

`Probability's Friend` should appear at the point where the reader most needs a
method system: after a pain point, inside a solution, or after evidence.

Required ideas when relevant:

- It is Bridge Doctor's authored work.
- It contains the Kuanlun knowledge system.
- It explains practical concepts such as elastic theory, QR value, CDVA typing,
  and wave-fish in plain language.

Do not force book promotion into the ending if another location is more natural.

## Image Rules

Content images:

- Use web-accessible URLs where possible.
- Add `border-radius: 8px`.
- Ensure the image topic matches the article.

Local QR/book/freebie assets:

- Use HTML `<img>` tags where the renderer supports local assets.
- Do not use Markdown `![](C:/...)` for local files.

Stale instruction to avoid: "use Markdown local image paths for WeChat images".

## Required Ending Modules

Include only when appropriate for the article and publishing context:

1. QR or assistant call-to-action.
2. Free-resource/freebie block.
3. `Probability's Friend` block if it was not integrated earlier.
4. Short thanks line.
5. Investment-risk disclaimer.

Minimum disclaimer:

```markdown
*免责声明：本文介绍的是量化分析技术与方法论，不构成投资建议。投资有风险，入市需谨慎。*
```

## Publish Command

Publish only after audit passes:

```js
mcp__wenyan-mcp__publish_article({
  file: "C:\\Users\\anzib\\wechat-articles\\article-file.md",
  theme_id: "orangeheart"
})
```

Do not use `default` theme.

## Audit Checklist

Reject publishing if any item fails:

- Title is over 64 characters.
- Article lacks disclaimer.
- Article implies investment advice, stock tips, guaranteed results, or advisory service.
- Data, people, dates, or outcomes are invented.
- Claims using approved data lack a source label.
- Kuanlun is positioned as investment training/advisory rather than quant-analysis training.
- Local images use Markdown `![](C:/...)` and may render as path text.
- Publishing theme is not `orangeheart`.

Report blocking issues before style issues.
