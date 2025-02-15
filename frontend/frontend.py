import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("AI ChatBot Agents")
st.write("Create and Interact with the AI Agents")

# User Input Fields
system_prompt = st.text_area("Define Your AI Agent:", height=70, placeholder="Type your system prompt here...")

# Model Selection
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama3-70b-8192"]
MODEL_NAMES_GOOGLE = ["gemini-pro"]

provider = st.radio("Select Provider:", ("Groq", "GoogleAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "GoogleAI":
    selected_model = st.selectbox("Select GoogleAI Model:", MODEL_NAMES_GOOGLE)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query:", height=140, placeholder="Ask your query...")

# Backend API URL
API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        # Prepare the request payload
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        # Send request to FastAPI backend
        response = requests.post(API_URL, json=payload)

        # Display Response
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:               
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data['response']}")
        else:
            st.error("Failed to get response from AI Agent. Please try again.")
