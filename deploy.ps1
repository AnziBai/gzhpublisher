#!/usr/bin/env pwsh
# deploy.ps1 — 将仓库中的 agents 和 skills 部署到 ~/.claude/
# 用法：在 gzhpublisher 目录下运行 .\deploy.ps1

$ClaudeDir = "$env:USERPROFILE\.claude"
$RepoDir   = $PSScriptRoot

Write-Host "部署 agents..."
Copy-Item "$RepoDir\agents\*.md" "$ClaudeDir\agents\" -Force

Write-Host "部署 skills..."
if (-not (Test-Path "$ClaudeDir\skills\fuwei-geo")) {
    New-Item -ItemType Directory -Path "$ClaudeDir\skills\fuwei-geo" -Force | Out-Null
}
Copy-Item "$RepoDir\skills\fuwei-geo\*" "$ClaudeDir\skills\fuwei-geo\" -Recurse -Force

Write-Host ""
Write-Host "完成！已部署到 $ClaudeDir"
Write-Host "重启 Claude Code 后生效。"
