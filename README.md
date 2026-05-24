# 🧠 LLM Logging System

A Python-based system that logs and monitors interactions with Large Language Models (LLMs).  
It captures prompts, responses, timestamps, and helps analyze usage patterns.

---

## 🚀 Features
- Log LLM prompts and responses
- Timestamped request tracking
- Modular architecture (routes, services, utils)
- Easy integration with OpenAI API
- Environment-based configuration

---

## 🏗️ Project Structure
app/
tests/
logs/
run.py


---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/LLM_Logging_System.git
cd LLM_Logging_System
pip install -r requirements.txt

## 🏗️ Architecture Overview

The system follows a modular layered architecture:

Client Request
    ↓
API Layer (Routes)
    ↓
Service Layer (LLM Logic)
    ↓
Utility Layer (Logging System)
    ↓
Storage (Logs / Files)
Modules:
app/routes/ → API endpoints
app/services/ → LLM processing logic
app/utils/ → Logging utilities
logs/ → Stored logs
config.py → Configuration management
## 🗄️ Schema Design Decisions

Each log entry is stored in structured JSON format:

{
  "timestamp": "2026-05-24T10:30:00Z",
  "prompt": "User input",
  "response": "Model output",
  "model": "gpt-4",
  "tokens_used": 120
}

## Design choices:
JSON format for simplicity
Timestamp-based logging for traceability
Optional metadata fields for scalability

## ⚖️ Tradeoffs
File-based logging used instead of database → simpler but less scalable
Monolithic structure instead of microservices → easier development
JSON logs instead of relational schema → flexible but harder analytics

## 🚀 Improvements with More Time
Add database (PostgreSQL / MongoDB)
Build real-time dashboard (React frontend)
Add authentication system
Add analytics (token usage, cost tracking)
Dockerize the application
Add CI/CD pipeline using GitHub Actions

##🛠️ TECH STACK
Python
FastAPI / Flask
OpenAI API
JSON Logging
dotenv

👨‍💻 Author
Patan Thamanna 
