# Grok CLI — Daily Quest Scrape Prompt

Use this in Grok CLI to scrape AgentOn and related platforms for new quests.

---

```
Scrape the following sources for active crypto/AI agent bounties and quests:
1. https://app.agenton.io (or AgentOn quest board URL)
2. FluxA dashboard
3. Twitter/X search: from:AgentOn OR #AgentOnQuest since:yesterday

For each result:
- Title
- Reward amount
- Deadline
- Link
- One-line summary of what to do

Output as markdown table, sorted by reward amount descending.
Flag anything expiring within 24 hours.
```
