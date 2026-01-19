from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
title="Hello Tasks API",
version="0.1.0",
description="Proste API edukacyjne (backend + bezpieczeństwo).",
contact={"name": "Łukasz"},
)


app.include_router(router)