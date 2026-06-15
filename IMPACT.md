# Impact Statement

## The Problem This Solves

Nonprofits live and die by their ability to communicate impact. Funders want
to see outcomes. Donors want to feel the human weight behind the numbers.
Board members need compelling reports. Social media audiences respond to stories,
not spreadsheets.

Most small nonprofits have the data. What they don't have is the time, budget,
or communications staff to turn that data into stories that move people to act.

A two-person food bank has served 12,000 meals this quarter. They know that.
But writing a donor email that makes someone feel those 12,000 meals — that's
a different skill, and it's one most small nonprofits can't afford to hire for.

**This tool does that translation. Instantly. For any nonprofit, any program,
any audience.**

---

## Connection to Pacific Community Ventures

Pacific Community Ventures' Radiant Data Hub is committed to what their team
calls "re-humanizing data insights by blending qualitative and quantitative
data into powerful narratives that mobilize action."

That phrase — re-humanizing data — is the entire design philosophy of this tool.

Numbers without stories are just numbers. This tool takes the numbers that
nonprofits already have and wraps them in the human context that makes funders
fund, donors donate, and communities rally.

This is a direct implementation of PCV's stated mission — built as an open-source
tool that any CDFI, nonprofit, or community organization can use for free.

---

## Who This Is For

- A nonprofit executive director who needs a donor email by Friday and has no
  communications staff
- A CDFI preparing their annual report with strong data but weak narrative
- A grassroots organization that just completed a program and needs to report
  outcomes to their funder
- A social enterprise trying to grow their Instagram following with impact content
- A grant writer who needs compelling language to wrap around program statistics

---

## Why Three Formats Matter

The same data tells a different story depending on who's reading it and where:

**Donor emails** need emotional hooks, personal stories, and a clear ask.
A donor reading their inbox at 8pm needs to feel something in the first sentence.

**Annual reports** need professional credibility, structured narrative, and
data woven into prose. A foundation program officer reviewing 50 grant reports
needs to find the key outcomes quickly.

**Social media** needs to be platform-specific. Instagram rewards emotion, line
breaks, and hashtags. LinkedIn rewards insight, professional framing, and
thought leadership. The same data, written differently, performs completely
differently on each platform.

This tool generates all three — from the same intake form, in minutes.

---

## Ethical Design Principles

**No data fabrication:** Claude is explicitly instructed never to invent
statistics not provided in the intake form. Where data is missing, it uses
[INSERT: ...] placeholders.

**Composite stories, not fake quotes:** When the user doesn't provide a
specific beneficiary story, Claude creates a clearly composite narrative
based on the demographics provided — not a fabricated quote attributed to
a real person.

**Human review required:** Every output includes a clear disclaimer that
the story is AI-generated and requires staff review before publishing.

**Voice-matched:** The tool asks for the organization's communication style
and instructs Claude to match it throughout — so the output sounds like
the organization, not like an AI.

---

## Limitations

- **Requires honest input:** The tool is only as accurate as the data provided.
  Inflating numbers produces a polished story built on inaccurate data.
- **Not a substitute for authentic voice:** AI-generated stories need human
  editing to reflect the organization's true character and relationships.
- **Composite stories need sensitivity review:** Any narrative involving
  beneficiaries should be reviewed by program staff before publishing.
- **Platform algorithms change:** Social media best practices evolve quickly.
  Hashtag recommendations and format guidance may need updating over time.

---

## Future Development

- Web interface for nonprofits without technical staff
- Spanish language output for Latino-serving organizations
- Integration with common nonprofit databases (Salesforce Nonprofit, Bloomerang)
  to pull impact data automatically
- Video script format for YouTube and TikTok impact stories
- A/B testing framework for donor email subject lines
- Automated quarterly report generation from connected data sources

---

*Built with Anthropic's Claude API.*
*Inspired by Pacific Community Ventures' commitment to re-humanizing data.*
*Dedicated to every nonprofit communicator who has stared at a blank page
with a spreadsheet full of stories waiting to be told.*
