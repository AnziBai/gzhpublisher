# Skill Writing Standards

Sources:
- https://agentskills.io/skill-creation/best-practices
- https://agentskills.io/specification

Use this file when creating or revising skills in this repository.

## Principles

- Start from real expertise: derive skill instructions from actual tasks, project
  artifacts, code review feedback, failure cases, and runbooks.
- Spend context carefully: keep `SKILL.md` focused on what the agent would not know
  without the skill.
- Design coherent units: one skill should cover one composable class of work.
- Use moderate detail: concise stepwise procedures and a working example beat
  exhaustive background material.
- Use progressive disclosure: keep the entry file lean and move detailed guidance
  to directly linked `references/` files.
- Calibrate control: be strict for fragile operations and flexible for creative or
  context-sensitive choices.
- Provide defaults, not menus: pick the normal path and mention alternatives only
  as escape hatches.
- Favor procedures over declarations: teach how to solve the class of tasks, not a
  single answer.
- Include gotchas, templates, checklists, and validation loops where they prevent
  repeated mistakes.

## Repository Convention

- Skill file name: `SKILL.md`.
- Frontmatter: only `name` and `description`.
- Skill names: lowercase letters, numbers, and hyphens.
- The `description` must include what the skill does and the trigger contexts. Do
  not hide trigger guidance in the body.
- Keep `SKILL.md` as the router and core workflow. Put detailed playbooks in
  `references/`.
- Reference files must be linked directly from `SKILL.md` with clear "when to read"
  instructions.
- Do not create redundant README/quickstart/changelog files inside a skill folder.
- Use the two-strike gate from `self-evolution-memory-system.md`: one-off lessons
  become candidates; repeated lessons become skill rules.
- Hard user red lines may be added immediately to project memory and relevant
  skills.
- Put reusable executable logic under `scripts/`; scripts should be self-contained,
  provide clear errors, and handle edge cases gracefully.

## Checklist

- [ ] The skill is grounded in repository-specific knowledge, not generic advice.
- [ ] `SKILL.md` can be understood in one pass.
- [ ] Detailed reference material is split into direct reference files.
- [ ] The default workflow is obvious.
- [ ] Fragile steps have exact instructions.
- [ ] Creative steps explain goals and constraints, not over-prescribed prose.
- [ ] Gotchas capture known failure modes.
- [ ] Output formats use templates.
- [ ] Validation happens before final output or publishing.
- [ ] The update preserves existing capability.
