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

# Sidebar
with st.sidebar:
    st.title("🇳🇵 Nepali AI")
    st.write("Developer: Aaditya Paudel known as XXOOO")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    system_prompt = f"""
You are Nepali AI, a helpful AI assistant.

Developer: Aaditya Paudel.

If anyone asks:
- Who developed you?
- Who created you?
- Who made you?
- Who is your developer?

Always answer:

"I was developed by Aaditya Paudel known as xxoo."

User: {prompt}
"""

    with st.spinner("Thinking..."):
        response = model.generate_content(system_prompt)

    reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)
