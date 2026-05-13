---
name: email-drafter
description: Drafts professional internal and external emails and creates a draft in Outlook with subject and body pre-filled. Use whenever the user asks to write, draft, compose, or send an email.
---

# Email Drafter Skill

## Behavior

1. Identify intent, audience, and tone.
2. Generate email subject and body.
3. Save JSON to email_input.json with fields: subject, body, to.
4. Run script: python .github/skills/email-drafter/scripts/draft_outlook_email.py email_input.json
5. Outlook draft opens automatically.

## Writing rules
- Short paragraphs
- Clear call-to-action
- Internal tone: direct
- External tone: formal