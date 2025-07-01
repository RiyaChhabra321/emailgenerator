# emailgenerator

import streamlit as st
import requests

GROQ_API_KEY = st.secrets["api_key"]

st.set_page_config(page_title="Groq AI Email Generator", layout="centered")
st.title("📨 Email Generator using ⚡ Groq + LLaMA 3")

prompt = st.text_area("📝 What should the email be about?")
tone = st.selectbox("🎯 Choose the tone", [
                    "Formal", "Informal", "Friendly", "Persuasive"])

if st.button("Generate Email") and prompt:
    with st.spinner("Generating email using LLaMA 3..."):
        try:
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "llama3-70b-8192",
                "messages": [
                    {
                        "role": "system",
                        "content": f"You are an assistant that writes {tone.lower()} professional emails."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                                     headers=headers, json=data)

            result = response.json()
            email_text = result["choices"][0]["message"]["content"]
            st.success("✅ Here's your email:")
            st.write(email_text)

        except Exception as e:
            st.error(f"❌ Error: {e}")
