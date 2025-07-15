# 🧠 Reddit Persona Builder (LLM + Groq)

This project scrapes Reddit user activity (posts + comments) and generates a detailed psychological **user persona** using **Groq's ultra-fast LLaMA 3** large language model.

> 🚀  Automatically analyzes Reddit users like `kojied`, `Hungry-Move-6603`, or `spez` and generates behavioral profiles in `.txt` and `.pdf` formats.

---

## 📌 Features

- 🔎 Scrapes public Reddit data using **PRAW**
- ⚡ Uses **Groq API** with `llama3-8b-8192` (super fast & free)
- 🧠 Generates detailed persona:
  - Interests & hobbies
  - Communication style
  - Personality traits
  - Political & social leanings
  - Academic/professional background
- 📄 Outputs results as `.txt` and beautifully formatted `.pdf`
- 🔁 Works for multiple usernames in one go
- 🔐 Clean `.env` setup with `.gitignore` for security

---

## 📦 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/reddit-persona-builder.git

cd reddit-persona-builder2. Install Python Dependencies

### 2. pip install -r requirements.txt

### 3. Set Up Your .env File
   
Create a .env file in the root directory with the following content:

REDDIT_CLIENT_ID=your_reddit_client_id 

REDDIT_CLIENT_SECRET=your_reddit_client_secret

REDDIT_USER_AGENT=reddit-persona-builder

GROQ_API_KEY=gsk-your_groq_api_key

### 🚀 Run the Project

python main.py

### 🔁 Add Multiple Users

You can analyze multiple Reddit users by modifying main.py like this:

usernames = ["kojied", "Hungry-Move-6603", "spez"]

---

### 📂 Output Format

All generated files are stored inside the output/ folder:

- output
- kojied_persona.txt
- kojied_persona.pdf
- Hungry-Move-6603_persona.txt
- spez_persona.pdf

 ---

## 🧠 Example Use Case

This tool is useful for:

- AI personality analysis

- Behavior research

- Marketing or targeting studies

- Academic NLP projects
  
--- 

## 🤖 Tech Stack

Python

Reddit API (PRAW)

Groq API

LLaMA 3 (llama3-8b-8192)

FPDF (for PDF generation)

dotenv

---
