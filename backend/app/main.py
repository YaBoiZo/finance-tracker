from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI(
    title="Finance Tracker API",
    version="0.1.0",
    description="Local-first finance tracker backend",
)

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
