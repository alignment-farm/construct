# Repository operating contract

Read [README.md](README.md) before working in this repository. It owns the
project narrative, current state, authority order, working rules, and task
routing. Then read the README nearest the files you will touch.

## Required read order

1. `AGENTS.md`
2. `README.md`
3. The nearest directory `README.md`
4. Only the task-specific specification, findings, code, evidence, or active
   thread required for the work

Stop when the task's scope and authority are clear. Do not preload the archive
or previous lab.

Open only when the task requires it:

| Task | Source |
| --- | --- |
| Inherited vocabulary or two-plane lineage terms | [notes/previous/review/glossary.md](notes/previous/review/glossary.md) |
| Previous-lab ancestry | [notes/previous/README.md](notes/previous/README.md) |
| Archived documentary wording or former paths | [.archive/README.md](.archive/README.md) |

## Documentation maintenance

- `README.md` owns the whole-project story and current state.
- Directory READMEs explain only their local space and point to the owner of
  broader claims.
- Specifications own mechanism contracts; findings own bounded interpretations;
  ledgers and scorers own experimental verdicts.
- Threads preserve deliberation and never silently become authority.
- `.archive/` preserves superseded documentation and is not a current source.
- `notes/previous/` is inherited lineage and is not reorganized with current
  documentation.
- Do not duplicate status prose. Link to its owner and include only the local
  context needed to make the link meaningful.
- When moving documentation, preserve bytes in `.archive/`, update its manifest,
  repair live links, and run path/link checks.
- Preserve unrelated work in a dirty tree.
