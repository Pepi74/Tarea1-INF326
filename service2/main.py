from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(filename='/var/log/fastapi/service2.log', level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Acceso a servicio 2!")
    return {"message": "Hola desde servicio 2"}
