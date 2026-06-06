import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.routers import transactions, shifts

load_dotenv()

app = FastAPI(title="Greyvetro POS Core API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
app.include_router(shifts.router, prefix="/api/shifts", tags=["shifts"])


@app.get("/health")
def health():
    return {"status": "ok"}
