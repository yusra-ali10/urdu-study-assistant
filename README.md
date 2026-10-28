# 📚 Urdu Study Assistant

An AI study helper that turns any notes into a summary, key points, a quiz, or a simple explanation in **Roman Urdu, Urdu, or English**. Built for Hacktoberfest Hack Day (Sahiwal x Zeppelin Labs).

## Problem
Many students in Pakistan study from English notes and find them hard to understand and revise. Most AI study tools work best in English only and need internet or paid APIs.

## Features
- Summary of pasted notes
- Key points with simple explanations of hard terms
- 5-question multiple-choice quiz with answers
- "Explain like I'm 15" mode
- Output in Roman Urdu, Urdu script, or English
- Upload a photo of notes (multimodal)

## How AI is Used
The app uses **Gemma 4** (Google's open-weight multimodal model) through the Gemini API. Every feature sends the student's notes (text and/or a photo of handwritten or printed notes) plus the chosen output language to Gemma 4. The model reads the notes, then summarizes, simplifies, translates, and writes quiz questions. Without Gemma 4 the app has no function.

## Setup
1. Get a free API key from [Google AI Studio](https://aistudio.google.com).
2. Clone and install:
   ```
   git clone <your-repo-url>
   cd study-assistant
   pip install -r requirements.txt
   ```
3. Set your key (or paste it in the app sidebar):
   ```
   set GEMINI_API_KEY=your_key      # Windows
   export GEMINI_API_KEY=your_key   # Mac/Linux
   ```
4. Run:
   ```
   streamlit run app.py
   ```

## Demo
Add screenshots / demo video link here.

## Roadmap
- PDF upload
- Flashcards export
- Voice input

## License
MIT. See [LICENSE](LICENSE).
