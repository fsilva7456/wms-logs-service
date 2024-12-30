from fastapi import FastAPI
from .routers import logs

app = FastAPI(title="WMS Logs Service")

app.include_router(logs.router)

@app.get("/")
def root():
    return {"message": "Hello from wms-logs-service!"}