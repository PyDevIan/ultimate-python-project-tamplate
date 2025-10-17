from fastapi import FastAPI
from app.core.logging_setup import setup_logging
from loguru import logger
import sys

setup_logging()
app = FastAPI(title="Copier Scaffold App")


@app.get("/")
async def root():
    logger.info("Root endpoint hit.")
    return {"message": "🚀 Backend ready, Loguru online!"}
