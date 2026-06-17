# Impact Story Generator

An AI-powered tool that transforms raw nonprofit program data into compelling
human impact narratives — for donor emails, annual reports, and social media.

Built in alignment with Pacific Community Ventures' Radiant Data Hub mission
to "re-humanize data insights by blending qualitative and quantitative data
into powerful narratives that mobilize action."

Read the full impact statement: IMPACT.md

---

## The problem

Nonprofits have the data. What they rarely have is the time, budget, or
communications staff to turn that data into stories that move people to act.

This tool does that translation — from numbers to narrative — in minutes.

---

## Three output formats

Enter your program data once. Choose your format. Get a polished draft.

  1. DONOR EMAIL NEWSLETTER
     Subject line, opening hook with a human story, key impact numbers
     written conversationally, gratitude, and a clear call to action.
     Length: 250-350 words. Tone: warm, urgent, human.

  2. ANNUAL REPORT NARRATIVE
     Professional section with headline, context, program description,
     impact highlights in flowing prose, demographics, quote placeholder,
     and forward-looking close. Length: 300-400 words. Tone: credible,
     data-driven, suitable for funders and board members.

  3. SOCIAL MEDIA CAPTIONS
     Instagram: hook, line breaks, emoji, hashtags, engagement question.
     LinkedIn: professional tone, insight-driven, thought leadership angle.
     Both written from the same data, optimized for each platform.

After generating, the tool asks if you want another format from the same
data — so you can produce all three in one session.

---

## What you enter

  Section 1: Organization name, mission, location
  Section 2: Program name, description, time period
  Section 3: Key metrics — people served, outcomes, funding deployed
  Section 4: Demographics, geography, one representative story
  Section 5: Communication style, desired call to action

---

## Setup

Requirements: Python 3.9 or higher, Anthropic API key

  git clone https://github.com/sumaleesimmonds/impact-story-generator.git
  cd impact-story-generator
  pip3 install anthropic
  export ANTHROPIC_API_KEY="sk-ant-your-key-here"
  python3 generator.py

---

## Sample output (donor email excerpt)

  Subject: Maria found stability. Here is how you made that possible.

  Last spring, Maria walked into our office carrying two grocery bags —
  everything she owned. She had been sleeping on her sister's couch for
  three months after losing her job, and she didn't know where to turn.

  Today, Maria has a stable apartment, a job that pays a living wage,
  and — her words — "the first savings account I've ever had in my life."

  Maria is one of 847 families we served this year.

  Because of donors like you, our housing stability program helped
  families in Queens and the Bronx secure permanent housing, access
  employment support, and build the financial foundation they need
  to stay housed for good...

---

## Ethical design

  - Claude never fabricates statistics not provided in the intake form
  - Missing data triggers [INSERT: ...] placeholders, not invented numbers
  - Composite beneficiary stories are clearly framed, not fake quotes
  - Every output includes a disclaimer requiring human review before publishing
  - Voice-matched to the organization's stated communication style

---

## Project structure

  impact-story-generator/
  |__ generator.py                    Main tool
  |__ README.md                       This file
  |__ IMPACT.md                       Humanitarian impact statement
  |__ requirements.txt                Dependencies
  |__ impact_story_[format]_[date].txt  Generated after running

---

## Tags

ai anthropic claude python nonprofit social-impact storytelling
donor-communications annual-report social-media cdfi
pacific-community-ventures impact-measurement llm

---

## License

MIT — free to use and adapt. If this helps a nonprofit tell their story
better, that is the whole point.
