\---

name: email-drafter

description: Drafts professional internal and external emails AND automatically creates a draft in Outlook with subject and body pre-filled. Use this skill whenever the user asks to write, draft, compose, rewrite, improve, or send an email.

\---



\# Email Drafter Skill (with Outlook integration)



\## Purpose

Generate professional emails and open them as a pre-filled Outlook draft, so the user only needs to add the recipient and click Send.



\## Behavior



1\. Identify:

&#x20;  - Intent (status update, follow-up, request, escalation, etc.)

&#x20;  - Audience (internal/external)

&#x20;  - Tone (polite, assertive, professional, friendly, apologetic)



2\. Generate JSON with:

{

"subject": "Clear subject line",

"body": "Full email body with greeting + content + sign-off",

"to": ""

}



3\. Save JSON to a file called `email\_input.json` in current folder.



4\. Run script:

python .github/skills/email-drafter/scripts/draft\_outlook\_email.py email\_input.json

5. Outlook draft will automatically open with subject + body filled.



\## Writing Style

\- Short paragraphs (2–3 lines)

\- Clear call-to-action

\- Polished + human tone

\- Adjust formality based on internal vs external



\## Examples



\### Example 1 — Status update

User: Draft status update email to my manager.

→ Generate JSON → Run script → Outlook opens with draft ✅



\### Example 2 — External follow-up

User: Draft a follow-up email to a customer waiting on approval.

→ Generate polite tone → Outlook draft opens ✅

