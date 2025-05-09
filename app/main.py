from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Scalable LLM API")

# Register routes
app.include_router(router)