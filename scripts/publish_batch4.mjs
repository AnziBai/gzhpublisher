#!/usr/bin/env node
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

const base = "C:/Users/anzib/gzhpublisher/articles/published";
const articles = [
  "wechat_batch4_01_trading-as-craft.md",
  "wechat_batch4_02_chanlun-overmodified.md",
  "wechat_batch4_03_three-core-abilities.md",
  "wechat_batch4_04_daytrading-20min.md",
  "wechat_batch4_05_five-success-signals.md",
  "wechat_batch4_06_smallcap-survival.md",
  "wechat_batch4_07_kdj-false-signals.md",
  "wechat_batch4_08_turtle-ashare-failure.md",
  "wechat_batch4_09_stable-profit-system.md",
  "wechat_batch4_10_ashare-survival-instinct.md",
  "wechat_batch4_11_trading-as-craft-3stages.md",
  "wechat_batch4_12_chanlun-to-kuanlun.md",
  "wechat_batch4_13_three-things-done-right.md",
  "wechat_batch4_14_daytrading-reframe.md",
  "wechat_batch4_15_amateur-to-pro-5things.md",
  "wechat_batch4_16_smallcap-three-tools.md",
  "wechat_batch4_17_kdj-as-filter.md",
  "wechat_batch4_18_turtle-bankruptcy-lesson.md",
  "wechat_batch4_19_rebuild-system-with-kuanlun.md",
  "wechat_batch4_20_wave-theory-vs-kuanlun.md",
].map(f => `${base}/${f}`);

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
const failed = results.filter(r => !r.ok).length;
console.log(`\n成功: ${results.filter(r=>r.ok).length}/20，失败: ${failed}/20`);
