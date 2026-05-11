# Prepublish Checklist

Run this before calling `mcp__wenyan-mcp__publish_article`.

## File And Metadata

- Article file exists and is readable.
- Article has YAML frontmatter with a final `title`.
- Title is suitable for WeChat and under 64 characters.
- Article body is Markdown, not a pasted tool transcript.
- No placeholder text remains.

## Compliance

- No fabricated people, dates, media mentions, awards, trading results, or
  guaranteed outcomes.
- Kuanlun/QMACD claims stay within education, methodology, and quant-analysis
  tooling. They are not framed as stock tips or investment advice.
- Investment-risk disclaimer is present for trading or market content.
- Data points have source labels, or are clearly framed as examples.

## WeChat Rendering

- Theme is `orangeheart`.
- Content images use web-accessible URLs where possible.
- Local QR/book/freebie assets use supported HTML `<img>` tags, not local
  Markdown syntax.
- No raw `![](C:/...)`, `![](D:/...)`, or bare local image paths appear in the
  article.
- Required ending modules are present when the article promotes the book,
  Kuanlun, QMACD, QR value, CDVA, wave-fish, or training.

## Publish Gate

Publish only when all items above pass. If any blocker remains, fix the article
and re-check before publishing.
