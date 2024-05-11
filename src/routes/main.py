from settings import settings

from fastapi import APIRouter, Response, Depends, status

router = APIRouter()


@router.get(
    "/",
    tags=["default"],
    summary="index"
)
def index_api():
    return {
        "Hello": "CTBC",
        "version": settings.APP_VERSION,
    }


@router.get(
    "/hc",
    tags=["default"],
    summary="health check"
)
def hc():
    return Response(status_code=200)
