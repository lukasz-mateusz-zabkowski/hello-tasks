import app.db.base  # noqa: F401
from fastapi import FastAPI
from app.api.tasks import router as tasks_router

# from app.api.routes import router as api_router

app = FastAPI(
    title="Hello Tasks API",
    version="0.1.0",
    description="Proste API edukacyjne (backend + bezpieczeństwo).",
    contact={"name": "Łukasz"},
)

# jeden wspólny router (app/api/routes.py będzie agregował endpointy)
# app.include_router(api_router)

app.include_router(tasks_router)