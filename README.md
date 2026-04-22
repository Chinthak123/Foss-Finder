# Foss-Finder
<img width="1037" height="924" alt="image" src="https://github.com/user-attachments/assets/55b71bc5-f608-4d41-942a-8ee324f74c54" />

🧬 AI-Powered FOSS Finder

An intelligent web application that helps users discover Free and Open Source Software (FOSS) alternatives to proprietary tools. Built with Python, Streamlit, and powered by Llama 3.1 via the Groq API.
🚀 Overview

The AI-Powered FOSS Finder leverages Large Language Models (LLMs) to provide real-time, dynamic recommendations for open-source software. Unlike static databases, this tool can identify alternatives for a vast range of proprietary applications, providing descriptions and direct links to official project websites.
✨ Features

    Intelligent Recommendations: Uses Llama 3.1 to understand the core functionality of proprietary software and suggest the best FOSS matches.

    Dynamic UI: A clean, responsive interface built with Streamlit.

    Structured Data: Implements JSON-mode prompting to ensure consistent and reliable data parsing.

    Real-time Search: Instant results with a professional loading state (spinner).

🛠️ Tech Stack

    Frontend: Streamlit

    AI Model: Llama 3.1-8b-instant

    Backend: Python / Requests

    Data Format: JSON

📋 Prerequisites

    Python 3.8 or higher

    A Groq API Key (Get one at console.groq.com)

⚙️ Installation & Setup

    Clone the repository:
    Bash

    git clone https://github.com/your-username/foss-finder.git
    cd foss-finder

    Install dependencies:
    Bash

    pip install streamlit requests

    Set your API Key:
    For security, this app uses an environment variable for the API key.

        Linux/macOS: export GROQ_API_KEY='your_api_key_here'

        Windows (PowerShell): $env:GROQ_API_KEY='your_api_key_here'

    Run the application:
    Bash

    streamlit run fossf.py

🧠 Why This Architecture?

    Dynamic Knowledge: Traditional databases of alternatives often become outdated. Using an LLM ensures the tool knows about the latest FOSS releases and community shifts.

    JSON Mode Integration: By forcing the model to output structured JSON, we bridge the gap between unstructured AI responses and a reliable software UI.

    Privacy & Open Weights: While this demo uses an API, the choice of Llama 3.1 (an open-weights model) means the system could be migrated to a fully local environment (using Ollama) to support the FOSS mission of data sovereignty.

🤝 Contributing

Contributions are welcome! If you have ideas for features like license verification, feature-by-feature comparisons, or local model support, feel free to fork this repo and submit a PR.
