import { renderAndPublish } from "file:///C:/Users/anzib/AppData/Roaming/npm/node_modules/@wenyan-md/mcp/node_modules/@wenyan-md/core/dist/wrapper.js";
import fs from "node:fs/promises";
import path from "node:path";

const file = process.argv[2];
if (!file) { console.error("Usage: node publish_single.mjs <file>"); process.exit(1); }

const normalized = file.replace(/\\/g, "/");
const getInputContent = async (c, f) => ({
  content: await fs.readFile(f.replace(/\\/g, "/"), "utf-8"),
  absoluteDirPath: path.dirname(f.replace(/\\/g, "/")),
});

try {
  const mediaId = await renderAndPublish(null, {
    file: normalized,
    theme: "orangeheart",
    highlight: "solarized-light",
    macStyle: true,
    footnote: true,
    disableStdin: true,
    appId: "wx66987ef9887a994f",
  }, getInputContent);
  console.log("✓", mediaId);
} catch (e) {
  console.error("✗", e.message);
  process.exit(1);
}
