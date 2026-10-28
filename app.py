import os

import streamlit as st
from google import genai
from PIL import Image

LANGS = {
    "Roman Urdu": "Roman Urdu (Urdu written in English letters)",
    "Urdu": "Urdu script",
    "English": "simple English",
}

TASKS = {
    "Summary": "Write a short, clear summary of these study notes in 5-7 lines.",
    "Key Points": "Extract the most important key points as a bullet list (max 8). Explain hard terms simply.",
    "Quiz": (
        "Create 5 multiple-choice questions from these notes. "
        "Give 4 options (A-D) for each. After all questions, add an 'Answers' section "
        "with the correct option and a one-line reason."
    ),
    "Explain Like I'm 15": "Explain these notes in very simple words with a real-life example.",
}

st.set_page_config(page_title="Urdu Study Assistant", page_icon="📚")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Gemini API key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    model = st.text_input(
        "Gemma 4 model name",
        value=os.getenv("GEMMA_MODEL", "gemma-4-31b-it"),
        help="Check the exact Gemma 4 name in Google AI Studio's model list.",
    )


def ask_gemma(task: str, lang: str, notes: str, image) -> str:
    client = genai.Client(api_key=api_key)
    prompt = (
        "You are a friendly study assistant for students in Pakistan. "
        f"Always reply in {LANGS[lang]}. Use only the information in the notes or image. "
        "Do not invent facts.\n\n"
        f"TASK: {task}\n\n"
    )
    contents = [prompt]
    if notes.strip():
        contents.append(f"NOTES:\n{notes}")
    if image is not None:
        contents.append(image)
    resp = client.models.generate_content(model=model, contents=contents)
    return resp.text


st.title("📚 Urdu Study Assistant")
st.caption("Paste notes or upload a photo of your notes. Get a summary, key points, or a quiz in Roman Urdu, Urdu, or English. Powered by Gemma 4.")

lang = st.radio("Output language", list(LANGS), horizontal=True)
notes = st.text_area("Paste your notes here", height=200)
photo = st.file_uploader("...or upload a photo of your notes", type=["png", "jpg", "jpeg"])
image = Image.open(photo) if photo else None
if image is not None:
    st.image(image, caption="Uploaded notes", use_container_width=True)
task_name = st.selectbox("What do you want?", list(TASKS))

if st.button("Generate", type="primary"):
    if not api_key:
        st.warning("Add your Gemini API key in the sidebar.")
    elif len(notes.strip()) < 30 and image is None:
        st.warning("Paste a few sentences or upload a photo of your notes.")
    else:
        with st.spinner("Gemma 4 is thinking..."):
            try:
                st.markdown(ask_gemma(TASKS[task_name], lang, notes, image))
            except Exception as e:
                st.error(f"Request failed. Check the API key and model name. Details: {e}")
