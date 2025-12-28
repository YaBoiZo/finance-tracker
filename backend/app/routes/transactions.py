from fastapi import APIRouter
from datetime import date

router = APIRouter(prefix="/transactions", tags=["transactions"])

# fake in-memory data (temporary)
FAKE_TRANSACTIONS = [
    {"id": 1, "date": str(date.today()), "description": "Coffee", "amount": -4.50},
    {"id": 2, "date": str(date.today()), "description": "Paycheck", "amount": 1200.00},
]

@router.get("/")
def list_transactions():
    return FAKE_TRANSACTIONS
