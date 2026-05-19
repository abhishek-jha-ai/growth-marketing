from fastapi import APIRouter, Response, status

router = APIRouter()

@router.get("/verify-runtime-preview", status_code=status.HTTP_200_OK)
async def verify_runtime_preview():
    """
    Endpoint to verify monorepo runtime and preview continuity.
    Returns a simple JSON response indicating success.
    """
    return {"message": "Monorepo runtime and preview continuity verified successfully."}
