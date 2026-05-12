#!/usr/bin/env pwsh
param(
    [string]$TargetRepo = (Get-Location).Path,
    [string]$SourceRepo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
    [switch]$InstallPolicy,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$TargetRepo = (Resolve-Path $TargetRepo).Path
$SourceRepo = (Resolve-Path $SourceRepo).Path

git -C $TargetRepo rev-parse --show-toplevel *> $null
if ($LASTEXITCODE -ne 0) {
    throw "TargetRepo is not a git repository: $TargetRepo"
}

$HookSource = Join-Path $SourceRepo ".githooks"
$ScriptSource = Join-Path $SourceRepo "scripts\self_evolution_hook.ps1"

if (-not (Test-Path $HookSource)) {
    throw "Missing hook source directory: $HookSource"
}

if (-not (Test-Path $ScriptSource)) {
    throw "Missing hook script: $ScriptSource"
}

$HookTarget = Join-Path $TargetRepo ".githooks"
$ScriptDir = Join-Path $TargetRepo "scripts"
$ScriptTarget = Join-Path $ScriptDir "self_evolution_hook.ps1"

if (-not (Test-Path $HookTarget)) {
    New-Item -ItemType Directory -Path $HookTarget -Force | Out-Null
}

if (-not (Test-Path $ScriptDir)) {
    New-Item -ItemType Directory -Path $ScriptDir -Force | Out-Null
}

Copy-Item (Join-Path $HookSource "*") $HookTarget -Force

if ((Test-Path $ScriptTarget) -and -not $Force) {
    Write-Host "Keeping existing $ScriptTarget. Use -Force to overwrite."
} else {
    Copy-Item $ScriptSource $ScriptTarget -Force
}

git -C $TargetRepo config core.hooksPath .githooks

if ($InstallPolicy) {
    $PolicySource = Join-Path $SourceRepo "docs\self-evolution-memory-system.md"
    $PolicyTargetDir = Join-Path $TargetRepo "docs"
    $PolicyTarget = Join-Path $PolicyTargetDir "self-evolution-memory-system.md"
    $AgentsTarget = Join-Path $TargetRepo "AGENTS.md"

    if (-not (Test-Path $PolicyTargetDir)) {
        New-Item -ItemType Directory -Path $PolicyTargetDir -Force | Out-Null
    }

    if ((Test-Path $PolicyTarget) -and -not $Force) {
        Write-Host "Keeping existing $PolicyTarget. Use -Force to overwrite."
    } else {
        Copy-Item $PolicySource $PolicyTarget -Force
    }

    if (-not (Test-Path $AgentsTarget)) {
        @"
# Agent Memory

This project uses hook-assisted self-evolution reminders.

## Stage-Close Protocol

1. If `.git/self-evolution-pending.md` exists, treat it as a reminder to review
   memory, docs, wiki knowledge, and skill candidates.
2. Run the `self-evolution` skill.
3. Produce a proposal before changing project memory, preference memory, wiki
   knowledge, or skills.
4. Store project-specific facts locally, not in global memory, unless the user
   confirms they are cross-project preferences.
"@ | Set-Content -Path $AgentsTarget -Encoding UTF8
    } else {
        Write-Host "AGENTS.md already exists. Add the stage-close protocol manually if needed."
    }
}

Write-Host ""
Write-Host "Self-evolution hooks installed."
Write-Host "Target repo: $TargetRepo"
Write-Host "core.hooksPath: $(git -C $TargetRepo config --get core.hooksPath)"
Write-Host "Hooks: $HookTarget"
Write-Host "Hook script: $ScriptTarget"
if (-not $InstallPolicy) {
    Write-Host "Tip: rerun with -InstallPolicy to copy the starter AGENTS.md/docs policy into a new project."
}
