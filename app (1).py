
import os
import gradio as gr
from openai import OpenAI


# =========================
# GROQ API CONFIGURATION
# =========================
from getpass import getpass
from openai import OpenAI

GROQ_API_KEY = getpass("Enter your Groq API key: ")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

print("Groq client configured successfully!")




# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
You are an expert learning roadmap designer.

Create personalized learning roadmaps based on:
- Domain
- Skill level
- Available learning time

The roadmap must be practical, realistic, structured,
easy to follow, and appropriate for the learner's level.

Always include:

1. Roadmap Overview
2. Learning Phases
3. Timeline
4. Topics to Learn
5. Practice Activities
6. Practical Projects
7. Tools and Technologies
8. Expected Outcomes
9. Next Steps

Prioritize important skills and avoid unnecessary topics.
"""


# =========================
# ROADMAP GENERATOR
# =========================

def generate_roadmap(domain, level, time):

    if not domain.strip():
        return "❌ Please enter a domain or field."

    user_prompt = f"""
Create a personalized learning roadmap.

Domain: {domain}
Skill Level: {level}
Available Learning Time: {time}

Create a realistic roadmap that matches this learner.

Explain:
- What they should learn
- In what order they should learn it
- What they should practice
- What projects they should build
- What tools they should learn

Use clear headings, bullet points, and tables where useful.
"""

    try:

        response = client.responses.create(
            model="openai/gpt-oss-20b",
            instructions=SYSTEM_PROMPT,
            input=user_prompt
        )

        return response.output_text

    except Exception as e:

        return f"❌ Error: {str(e)}"


# =========================
# GRADIO INTERFACE
# =========================

with gr.Blocks(
    title="AI Learning Roadmap Generator"
) as app:

    gr.Markdown("""
    # 🚀 AI Learning Roadmap Generator

    Create a personalized learning roadmap using AI.
    """)

    domain = gr.Textbox(
        label="📚 Domain / Field",
        placeholder="Example: Data Analysis"
    )

    level = gr.Dropdown(
        choices=[
            "Beginner",
            "Intermediate",
            "Advanced"
        ],
        value="Beginner",
        label="🎯 Skill Level"
    )

    time = gr.Dropdown(
        choices=[
            "1 Month",
            "3 Months",
            "6 Months",
            "1 Year"
        ],
        value="3 Months",
        label="⏱️ Learning Time"
    )

    generate_button = gr.Button(
        "🚀 Generate Roadmap"
    )

    roadmap_output = gr.Markdown()

    generate_button.click(
        fn=generate_roadmap,
        inputs=[domain, level, time],
        outputs=roadmap_output
    )


# =========================
# LAUNCH
# =========================

app.launch(share=True)
