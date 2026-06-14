from scalar_fastapi import get_scalar_api_reference
from starlette.responses import RedirectResponse

from src import app

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse("/docs")

@app.get("/docs", include_in_schema=False)
def read_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url
    )

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)