# 🚀 Scalable LLM API Backend

A production-ready, scalable backend system for serving LLM predictions using FastAPI, Redis, and Docker. Ideal for tasks such as document Q&A, summarization, and real-time NLP tasks.

---

## 🧠 Features

- ⚡️ **FastAPI** backend with async support
- 🧠 **LLM integration** via Hugging Face API or local model (e.g. `BAAI/bge-m3`)
- 🔁 **Retry logic** with exponential backoff
- 💾 **Redis caching** to optimize repeated requests
- 🐳 **Docker + Docker Compose** setup
- 🔐 **.env-based config** for secrets and API keys
- ✅ **Ready for production** use or customization

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI entry
│   ├── routes.py            # API endpoints
│   ├── llm_utils.py         # LLM wrapper
│   ├── cache.py             # Redis cache layer
│   └── config.py            # Env and settings
├── .env                     # API keys and configs
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```



---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/scalable-llm-api.git
cd scalable-llm-api