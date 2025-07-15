# 🧠 Reddit Persona Builder (LLM + Groq)

This project scrapes Reddit user activity (posts + comments) and generates a detailed psychological **user persona** using **Groq's ultra-fast LLaMA 3** large language model.

> 🚀  Automatically analyzes Reddit users like `kojied`, `Hungry-Move-6603`, or `spez` and generates behavioral profiles in `.txt` and `.pdf` formats.

---

## 🤖 Tech Stack

| Technology         | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **Python**         | Core language for scripting, scraping, and automation                  |
| **PRAW**           | Python Reddit API Wrapper to fetch posts and comments from Reddit      |
| **Groq API**       | Ultra-fast inference API to access LLaMA 3 models for persona analysis |
| **LLaMA 3 (8B)**   | Powerful open-source LLM model (`llama3-8b-8192`) used for reasoning   |
| **FPDF**           | Python library to convert generated persona into clean PDF format      |
| **dotenv**         | Loads API keys securely from `.env` file without exposing them         |

---

## 📌 Features

- 🧠 **Intelligent Persona Generation**  
  Analyzes user tone, interests, behavior, and psychology using LLaMA 3 via Groq.

- 🔍 **Reddit Scraping with PRAW**  
  Fetches latest posts and comments from any public Reddit profile (up to 100 each).

- ⚡ **Ultra-Fast LLM via Groq API**  
  Uses `llama3-8b-8192` — blazing-fast open-source model hosted on Groq’s API (no OpenAI billing needed).

- 📄 **Multi-format Output**  
  Generates clean `.txt` files and professional `.pdf` reports using FPDF.

- 🔁 **Bulk User Processing**  
  Supports multiple usernames in a single run — no need to restart the script.

- 🔐 **Secure Key Management**  
  API keys and credentials are safely loaded via `.env` and ignored in version control with `.gitignore`.

- 🧰 **Lightweight & Easy to Use**  
  Minimal setup, no frontend required — pure Python + command-line.

---

## 📦 Setup Instructions

### 🧲 1. Clone the Repository


git clone https://github.com/dhairya-0209/reddit-persona-builder.git

cd reddit-persona-builder

### 📦 2. Install Python Dependencies

pip install -r requirements.txt

This command installs all the required libraries from requirements.txt, including:

Package	Purpose
- praw	Reddit scraping using Python Reddit API Wrapper

- groq	Connects to Groq's ultra-fast LLaMA 3 models

- python-dotenv	Loads your API keys securely from a .env file

- fpdf	Generates clean PDF versions of the persona output

✅ Recommended: Use Python 3.8+ and a virtual environment for clean setup.

### 🔐 3. Set Up Your .env File

In the root directory, create a file named .env and paste your keys:

REDDIT_CLIENT_ID=your_reddit_client_id

REDDIT_CLIENT_SECRET=your_reddit_client_secret

REDDIT_USER_AGENT=reddit-persona-builder

GROQ_API_KEY=gsk-your_groq_api_key

🔒 This file is ignored by Git and keeps your keys safe.

### 🚀 4. Run the Project

Once setup is done, run:

python main.py

The program will:

Scrape Reddit user data (posts + comments)

Generate a detailed persona using LLaMA 3 via Groq

Save the result in both .txt and .pdf formats under /output

### 🔁 5. Analyze Multiple Reddit Users (Optional)

To analyze more than one user in a single run, edit the usernames list in main.py:

usernames = ["kojied", "Hungry-Move-6603", "spez"]

It will loop through each username and create separate output files automatically.

---

### 📂 Output Format

All generated files are stored inside the output/ folder:

- output
- kojied_persona.txt
- kojied_persona.pdf
- Hungry-Move-6603_persona.txt
- spez_persona.pdf

 ---

## 🧠 Example Use Cases

This tool can be a game-changer for:

- 🧪 **AI Research & Personality Analysis**  
  Automatically generate psychological profiles for user modeling or chatbot fine-tuning.

- 📊 **Behavioral & Social Media Research**  
  Understand how individuals express themselves across different Reddit communities.

- 🎯 **Marketing & Audience Targeting**  
  Identify potential user interests, tone, and personality for brand alignment.

- 🎓 **Academic NLP Projects**  
  Great for sentiment analysis, social behavior tracking, and LLM applications in real-world data.

---

## 🚀 Why This Project Stands Out

- ✅ End-to-end automated — from scraping to persona generation
- ✅ Powered by open-source LLMs (LLaMA 3) — no OpenAI costs
- ✅ Developer-friendly, fast, and secure
- ✅ Clean, extensible Python code ready for production or research

---

## ✨ Final Note

This project blends NLP, LLMs, and real-world user behavior to deliver **insightful, explainable, and real personas** — all with just a few lines of code.

 ---


