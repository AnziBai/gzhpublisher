#!/usr/bin/env pwsh
# Deploy repository agents and skills to ~/.claude/.
# Run from the gzhpublisher repository with: .\deploy.ps1

$ClaudeDir = "$env:USERPROFILE\.claude"
$RepoDir = $PSScriptRoot

$AgentsDir = Join-Path $ClaudeDir "agents"
$SkillsDir = Join-Path $ClaudeDir "skills"

if (-not (Test-Path $AgentsDir)) {
    New-Item -ItemType Directory -Path $AgentsDir -Force | Out-Null
}

if (-not (Test-Path $SkillsDir)) {
    New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
}

Write-Host "Deploying agents..."
Copy-Item (Join-Path $RepoDir "agents\*.md") $AgentsDir -Force

Write-Host "Deploying skills..."
Get-ChildItem -Path (Join-Path $RepoDir "skills") -Directory | ForEach-Object {
    $SkillName = $_.Name
    $SkillDest = Join-Path $SkillsDir $SkillName

    if (-not (Test-Path $SkillDest)) {
        New-Item -ItemType Directory -Path $SkillDest -Force | Out-Null
    }

    Copy-Item (Join-Path $_.FullName "*") $SkillDest -Recurse -Force
    Write-Host "  - $SkillName"
}

Write-Host ""
Write-Host "Done. Deployed to $ClaudeDir"
Write-Host "Restart Claude Code for changes to take effect."
