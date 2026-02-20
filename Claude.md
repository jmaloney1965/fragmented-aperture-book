## Memory Management — MANDATORY

Memory files live at: `/Users/jim.maloney/.claude/projects/-Users-jim-maloney-Book/memory/`

### At START of every session:
1. Read `MEMORY.md` (loaded automatically)
2. Read `session-status.md` for where we left off
3. Read `chapter-status.md` for current chapter state

### At END of every session (BEFORE the conversation ends):
1. **Always** update `session-status.md` with:
   - Date and what was accomplished
   - Files created or modified
   - Decisions made
   - Next steps
2. Update `chapter-status.md` if any chapter content or structure changed
3. Update `MEMORY.md` if new architectural decisions or key patterns were discovered

### When to update mid-session:
- After any commit
- After significant content is written or restructured
- After any chapter structure changes (renames, reorders, new chapters)

### Rules:
- Keep entries short: Date, what, why
- Don't wait to be asked — update proactively
- If the session produced commits, list them
- **If you skip this, the next session starts blind. Don't skip it.**
