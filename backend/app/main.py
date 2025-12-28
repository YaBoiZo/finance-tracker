from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.health import router as health_router

app = FastAPI(
    title="Finance Tracker API",
    version="0.1.0",
    description="Local-first finance tracker backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later we’ll lock this down
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "app": "finance-tracker"}
