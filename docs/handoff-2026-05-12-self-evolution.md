# 2026-05-12 Self-Evolution Handoff

This handoff records the current state of the self-evolution memory system and
workspace rename cleanup.

## Completed

- Added the `self-evolution` skill to gzhpublisher.
- Added hook-assisted stage-close reminders through `.githooks/` and
  `scripts/self_evolution_hook.ps1`.
- Added `scripts/install_self_evolution_hooks.ps1` so other projects can install
  the same hooks.
- Installed the hooks and starter policy files in these local projects:
  - `gzhpublisher`
  - `gzh-platform`
  - `New project 5`
  - `New project 6`

## Workspace Rename State

Codex workspace labels were read from
`C:\Users\Administrator\.codex\.codex-global-state.json`.

Completed local directory renames:

- `C:\Users\Administrator\Documents\New project` ->
  `C:\Users\Administrator\Documents\《概率的朋友》营销`
- `C:\Users\Administrator\Documents\New project 2` ->
  `C:\Users\Administrator\Documents\AI-autovideo`

Pending because Codex still has processes holding the directories:

- `C:\Users\Administrator\Documents\New project 3` ->
  `C:\Users\Administrator\Documents\Codex配置相关`
- `C:\Users\Administrator\Documents\New project 4` ->
  `C:\Users\Administrator\Documents\公众号发布系统`
- `C:\Users\Administrator\Documents\New project 5` ->
  `C:\Users\Administrator\Documents\自动化发布探索`

`New project 6` had no Codex workspace label and was not renamed.

## Pending Helper

One background helper should remain running:

```powershell
C:\Users\Administrator\Documents\finish_codex_project_rename.ps1
```

It waits for Codex processes to exit, finishes the pending renames, and updates
Codex workspace paths in `.codex-global-state.json`. It writes progress to:

```powershell
C:\Users\Administrator\Documents\finish_codex_project_rename.log
```

If Codex is already closed and the pending names still exist, run the helper
manually with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\Administrator\Documents\finish_codex_project_rename.ps1
```

The helper creates a timestamped backup of the Codex global state before editing
it.
