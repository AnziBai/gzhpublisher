# Publishing Runbook

This runbook captures the stable publishing behavior for gzhpublisher.

## Inputs

- `file`: absolute path to the final Markdown article.
- `theme_id`: always `orangeheart` for the Kuanlun public-account style.

Do not pass `app_id`, `content`, or other fields unless the repository
documentation is intentionally changed.

## Command

```js
mcp__wenyan-mcp__publish_article({
  file: "C:\\Users\\Administrator\\Documents\\New project 4\\gzhpublisher\\articles\\published\\article.md",
  theme_id: "orangeheart"
})
```

## Expected Result

The tool creates a draft in the WeChat Official Account draft box and returns a
Media ID. It does not perform the manual final send in the WeChat backend.

## Common Failures

- `40164` or IP whitelist error: update the WeChat Official Account API IP
  whitelist, then retry.
- Missing or wrong title: add or fix the YAML frontmatter `title`.
- Local image path appears as text: replace local Markdown image syntax with
  supported HTML image tags or web-accessible image URLs.
- Wrong theme or default styling: retry with `theme_id: "orangeheart"`.
- MCP unavailable: verify wenyan-mcp is running/configured in the current agent
  environment, then retry from the same article file.

## Reporting

Always report:

- absolute article path
- theme
- Media ID on success
- exact error and one concrete next step on failure
