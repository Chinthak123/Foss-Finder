import streamlit as st
import requests
import json
import os

API_URL = "https://api.groq.com/openai/v1/chat/completions" 
API_KEY = os.getenv("GROQ_API_KEY", "")

def get_foss_alternatives(software_name):
    """
    Sends a prompt to Llama to find FOSS alternatives.
    Returns a list of dictionaries.
    """
    
    prompt = f"""
    Find 3-4 Free and Open Source Software (FOSS) alternatives for: '{software_name}'.
    Return the results in a structured JSON format.

    Each item in the JSON list must have:
    - "name": Name of the software
    - "desc": A one-sentence description
    - "link": Official website URL

    Output ONLY the JSON object with a key named "alternatives".
    """

    if not API_KEY:
        st.error("Missing GROQ_API_KEY environment variable.")
        return None

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant", 
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"},
        "temperature": 0.2 
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code != 200:
            st.error(f"Groq API Detail: {response.text}")

        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']
        data = json.loads(content)
        return data.get("alternatives", [])
    except Exception as e:
        return None


st.set_page_config(page_title="AI FOSS Finder", page_icon="🧬")

st.title("🧬 AI-Powered FOSS Finder")
st.markdown("Enter any software to find its open-source counterparts using **Llama 3**.")


st.markdown("""
    <style>
    .foss-card {
        border: 1px solid #4a4a4a;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        background-color: #1e1e1e;
    }
    </style>
    """, unsafe_allow_html=True)


target_software = st.text_input("What proprietary software are you looking to replace?", 
                                placeholder="e.g. Adobe Premiere, Slack, MATLAB...")

if target_software:
    with st.spinner(f"Llama is analyzing '{target_software}'..."):
        results = get_foss_alternatives(target_software)

    if results and isinstance(results, list):
        st.subheader(f"Open Source Alternatives for {target_software}")
        
        
        for item in results:
            with st.container():
                st.markdown(f"### {item.get('name', 'Unknown')}")
                st.write(item.get('desc', 'No description available.'))
                st.link_button(f"Visit {item.get('name')} Website", item.get('link', '#'))
                st.write("---")
    else:
        st.info("No results found. Double-check your API key or the software name.")

with st.sidebar:
    st.header("Technical Overview")
    st.write("**Architecture:**")
    st.code("Streamlit <-> Llama API <-> JSON Parser")
    st.markdown("""
    **Why this approach?**
    - **Dynamic Knowledge:** Unlike a static database, the LLM knows about new FOSS projects.
    - **JSON Mode:** Used to bridge the gap between unstructured AI text and structured UI components.
    - **Extensibility:** Easy to add features like 'Compare Features' or 'License Type'.
    """)