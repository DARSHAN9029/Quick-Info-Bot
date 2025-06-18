# 🤖 Quick-Info Bot: Summarizer & Q&A from URL

This Streamlit-based intelligent bot can:

- 🎥 *Summarize YouTube videos* by extracting and processing their transcript text.
- 🌐 *Answer questions from any website* by analyzing its content.
- 💡 *Provide code snippets* if the user asks programming-related questions.

---

## Features

- *Automatic YouTube Transcript Summary*(Click "*Summarize*")
- *Website Question Answering using RAG principles*(Click "*Ask Questions*" after writnig the query)
- *Multi-page website scraping with BeautifulSoup*
- *Gemini 1.5 Flash* powered responses (via google.generativeai)
- *youtube_transcript_api* is used for collecting the transcripts
- *Streamlit UI* with image preview and friendly messages

---
## ⚙ Installation

### 1. Clone the repo
```
git clone https://github.com/DARSHAN9029/Quick-Info-Bot.git
cd quick-info-bot
```

### 2. Create virtual environment & install dependencies
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a .env file with your Gemini API Key:
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```
---
### Screenshots of working :
1. For Youtube video ( Summarizes the youtube video)
![Screenshot 2025-06-14 214945](https://github.com/user-attachments/assets/7139f813-cf80-4787-bb49-3b458dca220c)
![Screenshot 2025-06-14 215005](https://github.com/user-attachments/assets/8197a57b-b48f-49d2-9900-43bfeaac54ba)
---
2. For normal website ( answers the question asked related to website)
![Screenshot 2025-06-14 215034](https://github.com/user-attachments/assets/a05104be-a578-4285-a2a7-f62e8bbe2d21)
![Screenshot 2025-06-14 215044](https://github.com/user-attachments/assets/fd50df4d-a34c-4998-8141-d897761517ce)
