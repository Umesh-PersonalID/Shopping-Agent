import os
from functools import lru_cache
from pathlib import Path
# import boto3
from runtime import bootstrap_project_python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

# client = boto3.client('secretsmanager', region_name='your-region')
# response = client.get_secret_value(SecretId='prod/service/api-key')
# print(response['SecretString'])

bootstrap_project_python()

from schemas import RecommendationRequest
from services.recommendation_service import build_recommendation


app = FastAPI(title="Shopping Agent UI")
UI_FILE = Path(__file__).resolve().parent / "ui" / "index.html"


@lru_cache(maxsize=1)
def load_ui_html() -> str:
    return UI_FILE.read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return load_ui_html()


@app.post("/api/recommend")
def recommend(payload: RecommendationRequest):
    if not os.getenv("SERPAPI_API_KEY"):
        return JSONResponse(status_code=400, content={"detail": "SERPAPI_API_KEY is not configured."})

    if not os.getenv("OPENAI_API_KEY"):
        return JSONResponse(status_code=400, content={"detail": "OPENAI_API_KEY is not configured."})

    try:
        return build_recommendation(payload.query, payload.budget)
    except Exception as exc:
        return JSONResponse(status_code=500, content={"detail": str(exc)})


def main() -> None:
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", "8000")), reload=False)


if __name__ == "__main__":
    main()
