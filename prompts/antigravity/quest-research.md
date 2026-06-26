# Antigravity — Quest Research Prompt

Use this when you want Antigravity to go find new quests and populate `quests/active.md`.

---

```
Research all currently active quests and bounties available to an AgentOn Level 2 (Sparked) agent with handle cybergod.

Check:
1. AgentOn quest board — list all open quests with reward amounts, deadlines, and effort level.
2. FluxA — any active tasks or reward opportunities for bound agents.
3. Any partner platforms announced via AgentOn Twitter or Discord.

For each quest found, format it as:
### [Quest Name]
- Platform: [name]
- Reward: [amount in USDC or token]
- Deadline: [date or rolling]
- Effort: [Low/Medium/High]
- Task: [plain language — what do I actually do?]
- Deliverable: [what to submit and where]
- Status: Open

Output the full formatted list so it can be pasted directly into quests/active.md.

Also flag any quests that expire within 24 hours — mark them 🚨 URGENT.
```
