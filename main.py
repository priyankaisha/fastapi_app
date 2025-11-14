from fastapi import FastAPI
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def home():
    logger.info("Home API called")
    return {"Hello": "World"}

@app.get("/items/{name}")
def say_hello(name: str):
    logger.info(f"First API called with name={name}")
    return {"name": name}
