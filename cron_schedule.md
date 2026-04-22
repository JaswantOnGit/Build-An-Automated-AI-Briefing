# Cron Job Configuration

## Daily Briefing Schedule
Runs every weekday at 6:30 AM MST (America/Edmonton timezone).

## Cron Expression
```
30 6 * * 1-5
```
Breakdown: minute=30, hour=6, any day-of-month, any month, weekdays(1-5)

## Isolated Session Command (OpenClaw)
```bash
openclaw run --session isolated \
  --prompt "Search the web for the latest AI tools, AWS news, and project management trends.
  Summarize the top 3 findings for each topic. Format as a Telegram-friendly briefing
  and send it to my Telegram channel." \
  --model claude-sonnet \
  --timezone America/Edmonton
```

## Model Selection Guide
| Task | Model | Reason |
|------|-------|--------|
| Simple reminders/alerts | Claude Haiku | Fast, low cost |
| Daily research briefings | Claude Sonnet | Better reasoning and depth |

## Session Types
- **--session isolated**: Runs in a separate session, no context bleed with main chat. Best for automated tasks.
- **--session main**: Shares context with regular chat. Best for ongoing conversations.

## Security Notes
- Gateway must be running before cron fires
- Use isolated sessions to prevent context bleed
- Allowlist should be configured before enabling cron jobs
- Monitor API usage with /status command
