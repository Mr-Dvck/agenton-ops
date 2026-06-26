# NEW QUEST EXECUTION PROMPT

Use this when you have a specific quest you want Antigravity to execute. Fill in the blanks and paste.

---

```
ag, execute the following AgentOn quest completely.

## Quest Details
- Quest Name: [FILL IN]
- Platform: AgentOn
- Reward: [X] USDC
- Deadline: [DATE or ROLLING]
- Task: [Plain language description of what to do]
- Deliverable: [What to produce and where to submit it]

## Instructions
1. Complete the task to the highest quality possible.
2. Save the deliverable to outputs/[DATE]-[QUEST-NAME].md
3. If the deliverable requires submission to an external URL or form, use your browser sub-agent to submit it and capture confirmation.
4. Append the submission record to outputs/submissions-log.md
5. If reward is confirmed, add a row to wallet/payout-tracker.md

Do not ask questions. Execute and document.

[agenton-ops Gem]
```
