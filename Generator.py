#!/usr/bin/env python3
"""
impact-story-generator
=======================
An AI-powered tool that transforms raw nonprofit program data —
numbers, statistics, demographics, outcomes — into compelling human
impact narratives for three distinct audiences and formats:

    1. DONOR EMAIL    — A warm, story-driven newsletter email that
                        connects data to human lives and includes a
                        clear call to action for continued support.

    2. ANNUAL REPORT  — A professional, structured narrative section
                        ready to drop into an annual report or grant
                        report, with data woven into compelling prose.

    3. SOCIAL MEDIA   — Platform-optimized captions for Instagram and
                        LinkedIn, including suggested hashtags, that
                        turn program data into shareable, engaging posts.

The hardest part of nonprofit communications is not having the data —
it's turning numbers into stories that move people to act. This tool
does that translation automatically, while keeping the human voice and
organizational mission at the center.

Inspired by Pacific Community Ventures' Radiant Data Hub commitment to
"re-humanizing data insights by blending qualitative and quantitative
data into powerful narratives that mobilize action."

Usage:
    python3 generator.py

Author: Sumalee Simmonds
GitHub: https://github.com/maleechanel/impact-story-generator
"""

import anthropic
import datetime

# ─── Setup ────────────────────────────────────────────────────────────────────
client = anthropic.Anthropic()
MODEL  = "claude-sonnet-4-6"


# ─── Format Definitions ───────────────────────────────────────────────────────
# Each format has a name, description, and detailed writing instructions
# that Claude uses to tailor the output for the right audience and channel.

FORMATS = {
    "1": {
        "name": "Donor Email Newsletter",
        "description": "A warm, story-driven email to donors and supporters",
        "instructions": """Write a compelling donor email newsletter section about this program's impact.

Format requirements:
- Subject line (make it human and specific, not generic)
- Opening hook: Start with a specific person or moment (you can create a
  composite fictional beneficiary based on the demographics provided —
  use a name and brief detail to make it feel real)
- Bridge to data: Transition naturally from the story to the statistics
- Highlight 3-4 key impact numbers, written in plain conversational language
  (e.g. "That's 847 families" not "847 beneficiaries")
- Mission connection: 1-2 sentences tying the data back to the org's mission
- Gratitude: Thank donors genuinely and specifically
- Call to action: One clear, specific ask (donate, share, volunteer, etc.)
- Sign-off: Warm, personal, from the organization's voice
- Length: 250-350 words (not counting subject line)
- Tone: Warm, grateful, urgent but not desperate, human""",
    },

    "2": {
        "name": "Annual Report Narrative",
        "description": "A professional narrative section for an annual report or grant report",
        "instructions": """Write a professional annual report narrative section about this program's impact.

Format requirements:
- Section headline (bold, specific, data-driven — e.g. "847 Families Housed,
  One Neighborhood at a Time")
- Opening paragraph: Set the context — what problem does this program address?
  Use 1-2 compelling statistics about the broader issue to establish stakes.
- Program description: 2-3 sentences on how the program works
- Impact highlights: Present the key outcomes in flowing prose, not bullet points.
  Weave numbers into sentences naturally.
- Demographics section: Describe who was served with specificity and dignity
- Quote placeholder: Write [QUOTE FROM PROGRAM PARTICIPANT: one sentence describing
  what kind of quote would work best here, e.g. "Quote about how the program
  helped them find stable housing for the first time"]
- Looking ahead: 1-2 sentences on what comes next for the program
- Length: 300-400 words
- Tone: Professional, credible, data-driven but human, suitable for funders
  and board members""",
    },

    "3": {
        "name": "Social Media Captions",
        "description": "Captions for Instagram and LinkedIn with hashtags",
        "instructions": """Write two social media captions about this program's impact —
one for Instagram and one for LinkedIn.

INSTAGRAM CAPTION:
- Hook in the first line (before "more" cutoff — make it punchy)
- 3-5 short paragraphs with line breaks for readability
- Use 1-2 specific impact numbers but keep it human
- Emoji used sparingly but effectively (3-5 total)
- End with a question or call to action that encourages comments
- 15-20 relevant hashtags at the end
- Length: 150-220 words

LINKEDIN CAPTION:
- Professional but warm opening — not corporate speak
- 3-4 paragraphs telling the impact story
- Lead with the human angle, support with data
- No emoji (LinkedIn professional audience)
- End with a thought-provoking question or insight about the sector
- 5-8 professional hashtags
- Length: 180-250 words

Separate the two captions clearly with headers.""",
    },
}


# ─── Input Collection ─────────────────────────────────────────────────────────

def collect_program_data() -> dict:
    """
    Collect the nonprofit's program data through a structured intake form.

    Gathers organization info, program details, key metrics, demographics,
    and tone preferences — everything Claude needs to write an accurate,
    specific, and on-brand impact narrative.

    Returns:
        dict: Complete program data profile ready for story generation.
    """
    print("\n" + "=" * 62)
    print("  IMPACT STORY GENERATOR")
    print("  Turning your data into narratives that move people")
    print("=" * 62)
    print("""
  Answer each question as completely as you can.
  The more specific your data, the more powerful the story.
  Rough numbers are fine — just give your best estimate.
""")

    print("-" * 62)
    print("  SECTION 1: Your Organization")
    print("-" * 62)

    org_name    = input("\n  Organization name: ").strip()
    org_mission = input("  Mission (one sentence — what do you do and for whom?): ").strip()
    org_location = input("  City / region you serve: ").strip()

    print("\n" + "-" * 62)
    print("  SECTION 2: The Program")
    print("-" * 62)

    program_name = input("\n  Program name: ").strip()
    program_desc = input("  What does this program do? (2-3 sentences): ").strip()
    time_period  = input("  What time period does this data cover? (e.g. 2024, Q1 2025): ").strip()

    print("\n" + "-" * 62)
    print("  SECTION 3: Your Impact Numbers")
    print("-" * 62)
    print("  Enter your key metrics. Press Enter to skip any you don't have.\n")

    people_served    = input("  Total people / families / businesses served: ").strip()
    primary_outcome  = input("  Primary outcome achieved (e.g. jobs created, meals served, loans made): ").strip()
    outcome_number   = input("  Number for that outcome: ").strip()
    secondary_outcome = input("  Secondary outcome (optional): ").strip()
    secondary_number  = input("  Number for that outcome (optional): ").strip()
    total_funding    = input("  Total program funding or capital deployed (optional): $").strip()
    volunteer_hours  = input("  Volunteer hours contributed (optional): ").strip()

    print("\n" + "-" * 62)
    print("  SECTION 4: Who You Served")
    print("-" * 62)
    print("  Demographics help make the story specific and meaningful.\n")

    demographics = input("  Key demographics of people served (e.g. 70% women, 85% BIPOC, "
                         "60% immigrants): ").strip()
    geography    = input("  Neighborhoods, counties, or communities served: ").strip()
    one_story    = input("  Optional: Describe one real or representative person your "
                         "program helped (no names needed): ").strip()

    print("\n" + "-" * 62)
    print("  SECTION 5: Voice & Tone")
    print("-" * 62)

    org_voice = input("""
  How would you describe your organization's communication style?
  (e.g. "warm and community-focused", "professional and data-driven",
  "bold and advocacy-oriented", "hopeful and empowering"): """).strip()

    cta = input("\n  What do you want readers to DO after reading this? "
                "(e.g. donate, volunteer, share, visit our website): ").strip()

    return {
        "org_name":          org_name,
        "org_mission":       org_mission,
        "org_location":      org_location,
        "program_name":      program_name,
        "program_desc":      program_desc,
        "time_period":       time_period,
        "people_served":     people_served,
        "primary_outcome":   primary_outcome,
        "outcome_number":    outcome_number,
        "secondary_outcome": secondary_outcome,
        "secondary_number":  secondary_number,
        "total_funding":     total_funding,
        "volunteer_hours":   volunteer_hours,
        "demographics":      demographics,
        "geography":         geography,
        "one_story":         one_story,
        "org_voice":         org_voice,
        "cta":               cta,
    }


def choose_format() -> dict:
    """
    Prompt the user to select their desired output format.

    Returns:
        dict: The selected format definition including name,
              description, and writing instructions.
    """
    print("\n" + "=" * 62)
    print("  CHOOSE YOUR OUTPUT FORMAT")
    print("=" * 62)
    print()
    for key, fmt in FORMATS.items():
        print(f"  {key}. {fmt['name']}")
        print(f"     {fmt['description']}\n")

    while True:
        choice = input("  Enter 1, 2, or 3: ").strip()
        if choice in FORMATS:
            return FORMATS[choice]
        print("  Please enter 1, 2, or 3.")


# ─── Story Generation ─────────────────────────────────────────────────────────

def generate_story(data: dict, fmt: dict) -> str:
    """
    Send program data and format instructions to Claude to generate
    a polished, human impact narrative.

    Claude is prompted to act as an experienced nonprofit communications
    director who understands both data storytelling and the specific
    voice of the organization.

    Args:
        data (dict): Program data collected from collect_program_data().
        fmt  (dict): Selected format definition from FORMATS.

    Returns:
        str: The complete generated impact narrative, ready to review and use.
    """
    # Build a clean data summary to pass to Claude
    metrics_block = f"""
  People/businesses/families served: {data['people_served'] or 'Not provided'}
  Primary outcome: {data['primary_outcome']} — {data['outcome_number']}
  Secondary outcome: {data['secondary_outcome']} — {data['secondary_number']}
  Capital/funding deployed: ${data['total_funding'] or 'Not provided'}
  Volunteer hours: {data['volunteer_hours'] or 'Not provided'}"""

    story_prompt = f"""You are an experienced nonprofit communications director and impact storyteller.
Your specialty is transforming raw program data into narratives that make donors,
funders, and community members feel the human weight behind the numbers.

You are writing for {data['org_name']}, an organization with this mission:
"{data['org_mission']}"

Their communication style is: {data['org_voice'] or 'warm, human, and mission-focused'}
Their desired call to action: {data['cta'] or 'support our work'}

PROGRAM DATA:
  Organization: {data['org_name']}
  Location: {data['org_location']}
  Program: {data['program_name']}
  What it does: {data['program_desc']}
  Time period: {data['time_period']}

KEY METRICS:
{metrics_block}

WHO WAS SERVED:
  Demographics: {data['demographics'] or 'Not provided'}
  Geography: {data['geography'] or 'Not provided'}
  Representative story: {data['one_story'] or 'Not provided — create a brief composite based on demographics'}

YOUR TASK:
{fmt['instructions']}

Important guidelines:
- Never fabricate specific statistics not provided in the data above
- Where data is missing, write around it gracefully or use [INSERT: description of what to add]
- Match the organization's voice throughout
- Make the human impact feel real and specific, not generic
- Every number should feel meaningful, not just impressive
- Write this as if you know and deeply respect this organization's work

Begin writing now."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        messages=[{"role": "user", "content": story_prompt}],
    )

    return response.content[0].text


# ─── Save Output ──────────────────────────────────────────────────────────────

def save_output(data: dict, fmt: dict, story: str) -> str:
    """
    Save the generated impact story to a timestamped text file.

    Args:
        data  (dict): The program data profile.
        fmt   (dict): The selected format definition.
        story (str):  The generated narrative.

    Returns:
        str: The filename the story was saved to.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fmt_slug  = fmt["name"].lower().replace(" ", "_")
    filename  = f"impact_story_{fmt_slug}_{timestamp}.txt"

    header = f"""IMPACT STORY — {fmt['name'].upper()}
Generated by: Impact Story Generator
Powered by: Anthropic Claude AI
Inspired by: Pacific Community Ventures Radiant Data Hub
Date: {datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")}
Organization: {data.get('org_name', 'N/A')}
Program: {data.get('program_name', 'N/A')}
Period: {data.get('time_period', 'N/A')}

IMPORTANT: Review this draft carefully before publishing.
- Verify all statistics match your records exactly
- Fill in any [INSERT: ...] placeholders
- Edit to match your organization's specific voice
- Have a staff member or communications lead review before sending

{'=' * 62}

"""
    with open(filename, "w") as f:
        f.write(header)
        f.write(story)
        f.write(f"\n\n{'=' * 62}\n")
        f.write("Tips for using this story:\n")
        f.write("  - Add a real photo of your program or participants\n")
        f.write("  - Include your organization's logo and branding\n")
        f.write("  - Have a beneficiary review composite stories for accuracy\n")
        f.write("  - A/B test subject lines for email versions\n")
        f.write(f"\n  Saved: {filename}\n")

    return filename


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    """
    Run the full impact story generator workflow:
        1. Collect program data through structured intake
        2. User selects output format
        3. Claude generates the narrative
        4. Story is displayed and saved to file
        5. Option to generate another format from the same data
    """
    try:
        # Step 1: Collect data
        data = collect_program_data()

        while True:
            # Step 2: Choose format
            fmt = choose_format()

            # Step 3: Generate
            print("\n" + "=" * 62)
            print(f"  Writing your {fmt['name']}...")
            print("  This may take 15-20 seconds...")
            print("=" * 62)

            story = generate_story(data, fmt)

            # Step 4: Display
            print(f"\n{'=' * 62}")
            print(f"  YOUR {fmt['name'].upper()}")
            print(f"  {data.get('org_name', '')} — {data.get('program_name', '')}")
            print(f"{'=' * 62}\n")
            print(story)

            # Step 5: Save
            filename = save_output(data, fmt, story)
            print(f"\n{'=' * 62}")
            print(f"  Saved to: {filename}")
            print("  Review and personalize before publishing.")
            print(f"{'=' * 62}")

            # Offer to generate another format
            again = input("\n  Generate another format from the same data? [y/N]: ").strip().lower()
            if again != "y":
                print("\n  Your impact story is ready. Go tell it well. 🌟\n")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n\n  Session ended. Your data makes a difference — keep telling that story.\n")


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
