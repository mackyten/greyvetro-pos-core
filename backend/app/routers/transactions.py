from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth.dependencies import require_role
from app.models.user import TokenUser

router = APIRouter()


class TransactionRequest(BaseModel):
    amount: float
    item_ids: list[str] = []


@router.post("/")
async def create_transaction(
    payload: TransactionRequest,
    user: TokenUser = Depends(require_role("Cashier")),
):
    # TODO: persist transaction to database
    return {"status": "ok", "amount": payload.amount, "cashier": user.preferred_username}


@router.get("/")
async def list_transactions(_: TokenUser = Depends(require_role("ShiftLead"))):
    # TODO: query transactions for the current shift
    return []
