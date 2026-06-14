import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Nepali AI",
    layout="wide"
)

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🇳🇵 Nepali AI")
st.write("Developed by Aaditya Paudel")

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.write("You:", prompt)

    response = model.generate_content(prompt)

    st.write("AI:", response.text)
