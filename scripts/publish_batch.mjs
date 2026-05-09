#!/usr/bin/env node
// 批量发布文章到微信公众号草稿箱
// 需通过环境变量 WECHAT_APP_ID / WECHAT_APP_SECRET 提供凭据
import { renderAndPublish } from "file:///C:/Users/anzib/AppData/Roaming/npm/node_modules/@wenyan-md/mcp/node_modules/@wenyan-md/core/dist/wrapper.js";
import fs from "node:fs/promises";
import path from "node:path";

async function getInputContent(inputContent, file) {
  if (!inputContent && file) {
    const normalized = file.replace(/\\/g, "/");
    inputContent = await fs.readFile(normalized, "utf-8");
    return { content: inputContent, absoluteDirPath: path.dirname(normalized) };
  }
  return { content: inputContent, absoluteDirPath: undefined };
}

const articles = [
  "C:/Users/anzib/gzhpublisher/articles/published/交易做到这5点-说明你快要成功了.md",
  "C:/Users/anzib/gzhpublisher/articles/published/在股市活下来的人-都练成了这种本事.md",
  "C:/Users/anzib/gzhpublisher/articles/published/能稳定盈利的交易系统有多简单.md",
  "C:/Users/anzib/gzhpublisher/articles/published/亏了10万却舍不得花88元买书.md",
  "C:/Users/anzib/gzhpublisher/articles/published/散户学了3年还是亏钱-问题根本不在技术.md",
  "C:/Users/anzib/gzhpublisher/articles/published/你炒股的这5个习惯正在让你稳定亏钱.md",
  "C:/Users/anzib/gzhpublisher/articles/published/波浪理论为什么越学越亏-弹论才是正确用法.md",
  "C:/Users/anzib/gzhpublisher/articles/published/我见过亏损最惨的散户-都犯了这3个错误.md",
  "C:/Users/anzib/gzhpublisher/articles/published/交易是一门不求人的手艺.md",
  "C:/Users/anzib/gzhpublisher/articles/published/散户亏钱不是运气差-是认知欠费.md",
];

const results = [];

for (const article of articles) {
  const name = path.basename(article);
  try {
    const mediaId = await renderAndPublish(null, {
      file: article,
      theme: "orangeheart",
      highlight: "solarized-light",
      macStyle: true,
      footnote: true,
      disableStdin: true,
      appId: "wx66987ef9887a994f",
    }, getInputContent);
    console.log(`✓ ${name} → ${mediaId}`);
    results.push({ name, mediaId, ok: true });
  } catch (e) {
    console.error(`✗ ${name}: ${e.message}`);
    results.push({ name, error: e.message, ok: false });
  }
}

console.log("\n=== 发布结果摘要 ===");
results.forEach((r, i) => {
  if (r.ok) {
    console.log(`${i+1}. ✓ ${r.name}: ${r.mediaId}`);
  } else {
    console.log(`${i+1}. ✗ ${r.name}: ${r.error}`);
  }
});
