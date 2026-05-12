---
name: self-evolution
description: >
  Use when the user asks Codex to self-evolve, update memory, improve future
  behavior, run a stage-close reflection, decide what to remember, or turn
  repeated project lessons into skills or wiki knowledge.
---

# Self Evolution

Use this skill to decide what should become project memory, wiki knowledge,
preference memory, or a skill update. The default output is a proposal, not a
silent memory write.

## Start Here

1. Resolve the current project root from the working directory or `git rev-parse --show-toplevel`.
2. Read `<project-root>/AGENTS.md` for project red lines and memory boundaries.
3. Read `<project-root>/docs/self-evolution-memory-system.md` for the current policy.
   If either file is missing, propose creating it before storing long-term project
   memory.
4. Review the latest relevant work: changed files, user corrections, failed
   checks, repeated instructions, and published commits.
5. Classify each possible learning into one of the memory layers.
6. Output a memory update proposal and wait for confirmation before changing
   memory or skills, unless the user explicitly asked to implement the changes.

## Memory Layers

- Project memory: repository facts, workflows, commands, and red lines. Store in
  `AGENTS.md`, docs, and project skills.
- Wiki knowledge: external sources, research, and source-backed reusable methods.
  Store through `llm-wiki`.
- Preference memory: stable cross-project user preferences. Store only after
  user confirmation.
- Skill candidates: repeated procedures or mistakes that should become reusable
  skill rules.

## Promotion Gate

- One occurrence: candidate only.
- Two occurrences: update an existing skill if one fits.
- No fitting skill after two occurrences: propose a new skill.
- Hard user red lines or safety/compliance rules can be recorded immediately in
  project memory and relevant skills.

## Proposal Format

```markdown
## Memory Update Proposal

### Project Memory
- Add/update: ...
- Source: ...
- Boundary: ...

### Wiki Knowledge
- Add/update: ...
- Source: ...
- Boundary: ...

### Preference Memory
- Add/update: ...
- Confirmation needed: ...

### Skill Candidates
- Candidate: ...
- Strike count: ...
- Recommended action: ...
```

## Gotchas

- Do not turn task history into long-term memory unless it changes future
  behavior.
- Do not write project details into global memory by default.
- Do not create a new skill when an existing skill can be tightened.
- Do not let `SKILL.md` become a logbook; move detailed playbooks to
  `references/`.
- Preserve existing behavior when improving skill structure.
