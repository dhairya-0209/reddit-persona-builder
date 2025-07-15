import os
from dotenv import load_dotenv
from groq import Groq
from fpdf import FPDF  # ✅ NEW

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_user_persona(username, posts, comments, output_dir="output"):
    max_tokens = 5500  
    total_tokens = 0
    text_blocks = []

    def trim(text, limit=300):
        return text[:limit] + ("..." if len(text) > limit else "")

    for post in posts:
        if not post["selftext"]:
            continue
        block = f"Post: {trim(post['title'])}\n{trim(post['selftext'])}\nSource: {post['url']}\n"
        total_tokens += len(block.split())
        if total_tokens > max_tokens:
            break
        text_blocks.append(block)

    for comment in comments:
        block = f"Comment: {trim(comment['body'])}\nSource: {comment['url']}\n"
        total_tokens += len(block.split())
        if total_tokens > max_tokens:
            break
        text_blocks.append(block)

    text_corpus = "\n\n".join(text_blocks)

    prompt = f"""
You are an expert in psychological analysis and behavioral insights.
Based on the following Reddit activity by user u/{username}, generate a detailed persona.

Persona should include:
- Interests and hobbies
- Communication style
- Personality traits
- Political/social leanings
- Profession/academic background
- Other interesting observations

Cite specific posts/comments for each trait using the provided Source links.

Reddit Data:
{text_corpus}
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2048
        )

        persona = response.choices[0].message.content

        # ✅ Save to TXT
        os.makedirs(output_dir, exist_ok=True)
        txt_file = os.path.join(output_dir, f"{username}_persona.txt")
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(persona)
        print(f"✅ Persona saved to {txt_file}")

        # ✅ Save to PDF
        pdf_file = os.path.join(output_dir, f"{username}_persona.pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        for line in persona.split("\n"):
            pdf.multi_cell(0, 10, line)

        pdf.output(pdf_file)
        print(f"📄 PDF saved to {pdf_file}")

    except Exception as e:
        print("❌ Error generating persona:", e)
