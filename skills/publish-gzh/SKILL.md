---
name: publish-gzh
description: >
  Publish reviewed gzhpublisher/Kuanlun Markdown articles to the WeChat Official
  Account draft box through wenyan-mcp. Use when the user asks to publish, push
  to WeChat drafts, create a public-account draft, verify publish readiness, or
  troubleshoot WeChat publishing for this repository.
---

# Publish GZH

Use this skill for the final WeChat draft publishing step. It preserves the
existing gzhpublisher behavior: audit first, publish with `wenyan-mcp`, use the
`orangeheart` theme, and record the returned Media ID.

## Start Here

1. Identify the article Markdown file. Prefer files under `articles/published/`.
2. Read `references/prepublish-checklist.md` and resolve any blocking issue.
3. If publishing mechanics or error handling matter, read `references/publishing-runbook.md`.
4. Publish only after the article is ready for a WeChat draft.
5. Report the result with article path, theme, and Media ID or exact failure.

## Non-Negotiables

- Publish with `theme_id: "orangeheart"` unless project documentation is updated.
- Pass only `file` and `theme_id` to `mcp__wenyan-mcp__publish_article`.
- Do not pass `app_id`, `content`, or raw Markdown content.
- Do not publish if audit/compliance blockers remain.
- Do not use Markdown local image syntax such as `![](C:/...)`; local assets must
  use supported HTML image tags or be converted to web-accessible URLs.
- Treat WeChat draft creation as the final automated step. Manual final sending
  still happens in the WeChat Official Account backend.

## Default Publish Flow

```js
mcp__wenyan-mcp__publish_article({
  file: "C:\\Users\\Administrator\\Documents\\New project 4\\gzhpublisher\\articles\\published\\article.md",
  theme_id: "orangeheart"
})
```

After success:

- Capture the returned Media ID.
- Confirm the article is in the WeChat draft box.
- If the task includes a git checkpoint, commit the article and mention the
  Media ID in the commit message.

## Output Format

For successful publish:

```text
Published to WeChat draft box.
Article: <absolute path>
Theme: orangeheart
Media ID: <id>
```

For failed publish:

```text
Publish failed.
Article: <absolute path>
Theme: orangeheart
Error: <exact error>
Next step: <one concrete fix>
```

## References

- `references/prepublish-checklist.md`
- `references/publishing-runbook.md`
- `../fuwei-geo/references/wechat-article-workflow.md`
