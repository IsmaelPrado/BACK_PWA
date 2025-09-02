from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

@app.get("/openapi.yaml", include_in_schema=False)
def spec_yaml():
    return FileResponse("swagger.yaml", media_type="text/yaml")

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.yaml",
        title="Demo Docs",
    )

@app.get("/", include_in_schema=False)
def root():
    return HTMLResponse('<a href="/docs">Ir a /docs</a>')
