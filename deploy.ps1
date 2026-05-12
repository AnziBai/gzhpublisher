#!/usr/bin/env pwsh
# Deploy repository agents and skills to local agent skill directories.
# Run from the gzhpublisher repository with: .\deploy.ps1

$ClaudeDir = "$env:USERPROFILE\.claude"
$CodexDir = "$env:USERPROFILE\.codex"
$RepoDir = $PSScriptRoot

$AgentsDir = Join-Path $ClaudeDir "agents"
$ClaudeSkillsDir = Join-Path $ClaudeDir "skills"
$CodexSkillsDir = Join-Path $CodexDir "skills"

if (-not (Test-Path $AgentsDir)) {
    New-Item -ItemType Directory -Path $AgentsDir -Force | Out-Null
}

foreach ($Dir in @($ClaudeSkillsDir, $CodexSkillsDir)) {
    if (-not (Test-Path $Dir)) {
        New-Item -ItemType Directory -Path $Dir -Force | Out-Null
    }
}

Write-Host "Deploying agents..."
Copy-Item (Join-Path $RepoDir "agents\*.md") $AgentsDir -Force

Write-Host "Deploying skills..."
Get-ChildItem -Path (Join-Path $RepoDir "skills") -Directory | ForEach-Object {
    $SkillName = $_.Name

    foreach ($SkillsDir in @($ClaudeSkillsDir, $CodexSkillsDir)) {
        $SkillDest = Join-Path $SkillsDir $SkillName
        if (-not (Test-Path $SkillDest)) {
            New-Item -ItemType Directory -Path $SkillDest -Force | Out-Null
        }
        Copy-Item (Join-Path $_.FullName "*") $SkillDest -Recurse -Force
    }

    Write-Host "  - $SkillName"
}

Write-Host "Configuring git hooks..."
git -C $RepoDir config core.hooksPath .githooks
Write-Host "  - core.hooksPath=.githooks"

Write-Host ""
Write-Host "Done. Deployed skills to $ClaudeSkillsDir and $CodexSkillsDir"
Write-Host "Restart Claude Code or Codex for changes to take effect."
