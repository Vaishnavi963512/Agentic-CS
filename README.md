# 🌍 Weather AI Agent (FastAPI + OpenRouter)

## 📌 Overview

This project is a simple AI agent that answers weather-related questions.
It uses an LLM to understand user input, extract the city name, and fetch real-time weather data using the OpenWeather API.

The system demonstrates how an AI model can work with external tools to provide accurate and dynamic responses.

---

## 🚀 Features

* 🌐 User-friendly web interface using FastAPI
* 🧠 LLM-based understanding of user queries
* 📍 Automatic city extraction from natural language
* 🌦️ Real-time weather data using OpenWeather API
* 🔗 Integration of LLM with external tools

---

## 🏗️ Architecture

User → FastAPI → LLM (city extraction) → Weather Tool → API Call → Response

---

## ⚙️ Tech Stack

* Python
* FastAPI
* OpenRouter (LLM API)
* OpenWeather API
* Requests

---

## 🔄 Workflow

1. User enters a weather-related question
2. FastAPI receives input
3. LLM extracts the city name
4. Extracted city is passed to weather tool
5. Tool calls OpenWeather API
6. Weather data is fetched
7. Final response is displayed to user

---

## ▶️ How to Run

### 1. Clone the repository

```bash id="knt4zp"
git clone https://github.com/Vaishnavi963512/Agentic-CS.git
cd Agentic-CS
```

### 2. Create virtual environment

```bash id="u8hycz"
python -m venv ai_env
ai_env\Scripts\activate
```

### 3. Install dependencies

```bash id="o5fzjt"
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file:

```id="4fce0i"
OPENWEATHER_API_KEY=your_key
OPENROUTER_API_KEY=your_key
```

---

### 5. Run the application

```bash id="b0kdfq"
uvicorn main:app --reload
```

---

### 6. Open in browser

```id="vqk76n"
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```id="2cs37r"
├── main.py
├── agent.py
├── tools.py
├── requirements.txt
```

---

## 💡 Key Concepts

* AI Agents
* LLM + Tool Integration
* API Integration
* Prompt Engineering

---

## 🎯 Future Improvements

* Add multiple tools (news, maps, etc.)
* Improve UI design
* Add memory to agent
* Convert into multi-agent system

---

## 👩‍💻 Author

Vaishnavi Narayanam
GitHub: https://github.com/Vaishnavi963512
