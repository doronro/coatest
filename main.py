import os

from fastapi import FastAPI

enable_docs = os.environ.get("ENABLE_DOCS", "false").lower() == "true"

app = FastAPI(
    docs_url="/docs" if enable_docs else None,
    redoc_url="/redoc" if enable_docs else None,
    openapi_url="/openapi.json" if enable_docs else None,
)


@app.get("/")
def read_root():
    return {"message": "Hello World", "subtitle": "Version Test"}
