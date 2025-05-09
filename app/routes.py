from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.llm_utils import query_llm
from app.cache import get_cached_response, set_cached_response

router = APIRouter()

class QueryInput(BaseModel):
    query: str
    context: str

@router.post("/predict")
async def predict(input_data: QueryInput):
    cache_key = f"{input_data.query}_{hash(input_data.context)}"
    cached = await get_cached_response(cache_key)
    if cached:
        return {"result": cached, "cached": True}

    result = await query_llm(input_data.query, input_data.context)
    await set_cached_response(cache_key, result)
    return {"result": result, "cached": False}