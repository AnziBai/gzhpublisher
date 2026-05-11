---
name: fuwei-geo
description: >
  GEO and WeChat public-account content workflow for Kuanlun/QMACD. Use when the
  user wants AI-search/GEO strategy, brand-source building, AI visibility checks,
  WeChat article planning/writing/rewriting, viral article analysis, benchmark
  article ingestion, Kuanlun compliance review, or content intended to promote
  Probability's Friend, Kuanlun, QMACD, QR value, CDVA, wave-fish, or quant-analysis
  training. Also use when the user says they want content to be cited by AI,
  ranked in AI search, recommended by Doubao/DeepSeek/Qianwen/Kimi/Yuanbao, or
  published as a WeChat official-account draft.
---

# Fuwei GEO

Use this skill to turn Kuanlun brand knowledge, benchmark article patterns, and
WeChat publishing constraints into publishable content without inventing facts or
loading the entire knowledge base up front.

## Start Here

1. Classify the request.
   - GEO strategy, AI visibility, source-building, or keyword planning: use `references/geo-playbook.md`.
   - Kuanlun/QMACD brand facts, product positioning, compliance boundaries, or approved data: read `references/kuanlun-project-summary.md`.
   - WeChat article writing, rewriting, viral article analysis, publishing, or audit preparation: use `references/wechat-article-workflow.md`.
   - Baidu Baike brand/person entry: use the Baike template files under `references/`.
   - Benchmark article structure: read `references/benchmark-articles/index.md`, then only the specific benchmark file(s) needed.
2. Produce a short plan before generating or publishing content. Name the article type, target reader, evidence source, assets needed, and compliance risks.
3. Execute the relevant workflow. Prefer concrete defaults over asking the user to choose from a menu.
4. Validate with the checklist in the relevant reference before final output or publish.

## Non-Negotiables

- Do not invent people, dates, trading stories, profit numbers, survey results, media mentions, awards, or user outcomes.
- Use only approved factual data from `references/kuanlun-project-summary.md` or clearly label examples as technical demonstrations, not investment advice.
- Position Kuanlun as quant-analysis technology training and methodology education, not stock tips, investment advisory, or guaranteed profit.
- Every Kuanlun article must include an investment-risk disclaimer.
- WeChat publishing uses `theme_id="orangeheart"` only.
- For WeChat content images, prefer web-accessible URLs for content images. Local QR/book/freebie images may use HTML `<img>` tags when the publishing tool supports local assets.
- Do not use Markdown `![](C:/...)` for local images; it can degrade into visible path text in the WeChat renderer.

## Core Workflows

### GEO Strategy

Use `references/geo-playbook.md`.

Default sequence:
1. Define the entity: company, brand, product, person/IP, and canonical naming.
2. Build intent terms: product terms, problem terms, comparison terms, scenario terms, and decision terms.
3. Map source platforms: Baike/official site first, then ByteDance ecosystem, Q&A communities, free blogs, business directories, and vertical media.
4. Create content briefs by intent cluster.
5. Test AI visibility across Doubao, DeepSeek, Qianwen/Kimi/Yuanbao, and Wenxin where relevant.
6. Record what sources each AI cited and revise content/source coverage.

### WeChat Article Creation

Use `references/wechat-article-workflow.md` and `references/kuanlun-project-summary.md`.

Default sequence:
1. Identify article mode: original GEO article, benchmark rewrite, comparison article, method explainer, book-promotion article, or audit-only.
2. If rewriting from a benchmark, preserve the original hook, first-paragraph function, argument rhythm, and emotional curve. Change the subject naturally; do not do mechanical keyword replacement.
3. Write with conclusion-first structure, short paragraphs, concrete scenarios, and clear evidence.
4. Integrate Kuanlun/QMACD and `Probability's Friend` only where they solve a real pain point in the article.
5. Add approved visuals and the required ending modules.
6. Run the audit checklist before publish.

### Viral Article Analysis

Use benchmark articles as raw material, not as full-context payload.

Output:
```yaml
emotional_architecture:
  curve: ...
  density: ...
  psychological_needs: [...]
title_engineering:
  hook_type: ...
  reusable_formula: ...
opening_hook:
  mechanism: ...
  transferable_parts: [...]
rewrite_advice:
  keep: [...]
  adapt: [...]
  avoid: [...]
```

### Publishing

Publish only after the audit passes.

```js
mcp__wenyan-mcp__publish_article({
  file: "C:\\Users\\anzib\\wechat-articles\\article-file.md",
  theme_id: "orangeheart"
})
```

Never pass `app_id` to the publishing tool unless the project documentation is updated to require it.

## Output Standards

For articles:
- Markdown with YAML frontmatter.
- Title under 64 characters; prefer mobile-friendly length when possible.
- No prefatory explanation such as "Here is the article".
- Data has source labels.
- `Probability's Friend` promotion appears where it helps the argument, not as a forced ending.
- End with the required QR/free-resource/thanks/disclaimer modules described in `references/wechat-article-workflow.md`.

For audits:
- Lead with pass/fail.
- List blocking issues first.
- Include exact location, why it fails, and how to fix it.
- Reject publish if any zero-tolerance compliance issue appears.

## Gotchas

- The repository previously had a very large monolithic skill. Keep `SKILL.md` lean; move detailed guidance into direct reference files and load only what the task needs.
- `references/benchmark-articles/` can be large. Read the index first; then load only matching examples.
- If instructions conflict, follow this order: compliance boundaries in `references/kuanlun-project-summary.md`, WeChat renderer constraints in `references/wechat-article-workflow.md`, then general GEO strategy.
- Some older docs may mention Markdown local images or `default` theme. Treat those as stale; use HTML local image tags where needed and `orangeheart`.
