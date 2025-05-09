# app/logger.py
import logging

logger = logging.getLogger("llm_api")
logger.setLevel(logging.INFO)

# Console handler
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)