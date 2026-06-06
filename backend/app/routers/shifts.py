from fastapi import APIRouter, Depends
from app.auth.dependencies import require_role
from app.models.user import TokenUser

router = APIRouter()


@router.get("/")
async def list_shifts(_: TokenUser = Depends(require_role("ShiftLead"))):
    # TODO: query active shifts from database
    return []


@router.post("/open")
async def open_shift(user: TokenUser = Depends(require_role("ShiftLead"))):
    # TODO: create a new shift record
    return {"status": "opened", "lead": user.preferred_username}


@router.post("/close")
async def close_shift(user: TokenUser = Depends(require_role("ShiftLead"))):
    # TODO: close the active shift and summarise transactions
    return {"status": "closed", "lead": user.preferred_username}
