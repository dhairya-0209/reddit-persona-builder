# 🧠 Reddit Persona Builder (LLM + Groq)

This project scrapes Reddit user activity (posts + comments) and generates a detailed psychological **user persona** using **Groq's ultra-fast LLaMA 3** large language model.

> 🚀  Automatically analyzes Reddit users like `kojied`, `Hungry-Move-6603`, or `spez` and generates behavioral profiles in `.txt` and `.pdf` formats.

---

## 📌 Features

 🔎 Scrapes public Reddit data using **PRAW**
 
⚡ Uses **Groq API** with `llama3-8b-8192` (super fast & free)

🧠 Generates detailed persona:

  - Interests & hobbies
    
  - Communication style
   
  - Personality traits
    
  - Political & social leanings
    
  - Academic/professional background
    
 📄 Outputs results as `.txt` and beautifully formatted `.pdf`

 🔁 Works for multiple usernames in one go
 
 🔐 Clean `.env` setup with `.gitignore` for security

---

## 📦 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/reddit-persona-builder.git

cd reddit-persona-builder2. Install Python Dependencies

 ### 2. Install Python Dependencies  

> pip install -r requirements.txt
> 
> This command will install all the required libraries listed in the `requirements.txt` file, including:  

> - `praw` – for Reddit scraping
> -  
> - `groq` – to connect with Groq's LLaMA models
> -  
> - `python-dotenv` – to load API keys securely from `.env`
> -  
> - `fpdf` – to generate PDF reports of the persona  
> 
> Make sure you're using **Python 3.8 or above** and have a **virtual environment activated** (recommended).

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

| Technology         | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **Python**         | Core language for scripting, scraping, and automation                  |
| **PRAW**           | Python Reddit API Wrapper to fetch posts and comments from Reddit      |
| **Groq API**       | Ultra-fast inference API to access LLaMA 3 models for persona analysis |
| **LLaMA 3 (8B)**   | Powerful open-source LLM model (`llama3-8b-8192`) used for reasoning   |
| **FPDF**           | Python library to convert generated persona into clean PDF format      |
| **dotenv**         | Loads API keys securely from `.env` file without exposing them         |

---
