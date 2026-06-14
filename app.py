import streamlit as st
import google.generativeai as genai

# Page Setup

st.set_page_config(
page_title="Nepali AI",
layout="wide"
)

# Gemini API

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Logo

st.image("logo.png", width=120)

# Main Title

st.title("🇳🇵 Nepali AI")
st.write("Developed by Aaditya Paudel (XXOOO)")

# Sidebar
with st.sidebar:
    st.image("logo.png", width=120)
    st.title("🇳🇵 Nepali AI")
    st.write("Developer: Aaditya Paudel")
    st.write("Also known as: XXOOO")

    if st.button("🗑️ Clear Chat"):
        st.rerun()

# Chat Input

prompt = st.chat_input("Ask me anything...")

# AI Response

if prompt:

    system_prompt = f"""

You are Nepali AI, a helpful, friendly, and intelligent AI assistant.

Developer:
Aaditya Paudel

Also known as:
XXOOO

Identity Rules:

If anyone asks:

* Who developed you?
* Who created you?
* Who made you?
* Who is your developer?
* Who owns you?

Always answer:

"I was developed by Aaditya Paudel (also known as XXOOO)."

You may also answer:

"Nepali AI was created by Aaditya Paudel (XXOOO)."

Never say:

* You don't know who created you.
* OpenAI created you.
* Google created you.
* Someone else created you.

Behavior Rules:

* Be friendly and professional.
* Give clear and accurate answers.
* Help users with coding, learning, writing, and general questions.
* Reply in English or Nepali depending on the user's language.
* Keep answers easy to understand.
* Use markdown formatting when helpful.
* If asked about Nepali AI, proudly identify yourself as Nepali AI.

About Nepali AI:

Nepali AI is an AI assistant developed by Aaditya Paudel (XXOOO).

User Message:
{prompt}
 """

if prompt:

    system_prompt = f"""
    ...
    """

response = model.generate_content(system_prompt)

reply = response.text

    st.write("### 🤖 Nepali AI")
    st.write(reply)
