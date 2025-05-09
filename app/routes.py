from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_utils import query_llm
from app.cache import get_cached_response, set_cached_response
from app.logger import logger  

router = APIRouter()

class QueryInput(BaseModel):
    query: str
    context: str

@router.post("/predict")
async def predict(input_data: QueryInput):
    cache_key = f"{input_data.query}_{hash(input_data.context)}"

    logger.info(f"Received query: {input_data.query[:50]}...")


    cached = await get_cached_response(cache_key)
    if cached:
        logger.info("Cache hit")
        return {"result": cached, "cached": True}

    logger.info("Cache miss, calling LLM")
    result = await query_llm(input_data.query, input_data.context)
    await set_cached_response(cache_key, result)
    logger.info("LLM response cached")
    return {"result": result, "cached": False}