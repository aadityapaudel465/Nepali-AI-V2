import streamlit as st
import google.generativeai as genai

st.set_page_config(
page_title="Nepali AI",
page_icon="🇳🇵",
layout="wide"
)

# Custom CSS

st.markdown("""

<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #07111f);
}

h1, h2, h3 {
    color: white !important;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

.stChatMessage {
    border-radius: 15px;
}

div[data-testid="stChatInput"] {
    border-radius: 15px;
}

.block-container {
    padding-top: 2rem;
}
</style>

""", unsafe_allow_html=True)

# Gemini API

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Header

st.title("🇳🇵 Nepali AI")
st.write("Developed by Aaditya Paudel (AS KNOWN AS XXOOO)")

# Sidebar

with st.sidebar:

```
st.image("logo.png", width=120)

st.title("🇳🇵 Nepali AI")

st.write("Developer:")
st.write("Aaditya Paudel (XXOOO)")

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.markdown("---")

st.subheader("About")

st.write(
    "Nepali AI is an intelligent assistant powered by Google's Gemini model."
)

st.markdown("---")

st.subheader("Features")

st.write("🤖 Powered by Gemini")
st.write("💬 Chat History")
st.write("⚡ Fast Responses")
st.write("🇳🇵 Made in Nepal")
```

# Chat History

if "messages" not in st.session_state:
st.session_state.messages = []

# Display old messages

for message in st.session_state.messages:

```
avatar = "👤" if message["role"] == "user" else "logo.png"

with st.chat_message(message["role"], avatar=avatar):
    st.write(message["content"])
```

# User Input

prompt = st.chat_input("Ask me anything...")

if prompt:

```
st.session_state.messages.append(
    {"role": "user", "content": prompt}
)

with st.chat_message("user", avatar="👤"):
    st.write(prompt)

system_prompt = f"""
```

You are Nepali AI, a helpful AI assistant.

Developer: Aaditya Paudel.

If anyone asks:

* Who developed you?
* Who created you?
* Who made you?
* Who is your developer?

Always answer:

"I was developed by Aaditya Paudel."

You may also say:

"Nepali AI was created by Aaditya Paudel."

Never say you don't know who created you.

User: {prompt}
"""

```
with st.spinner("Thinking..."):
    response = model.generate_content(system_prompt)

reply = response.text

st.session_state.messages.append(
    {"role": "assistant", "content": reply}
)

with st.chat_message("assistant", avatar="logo.png"):
    st.write(reply)
```
