from settings import settings

from routes import main 

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import logging


app = FastAPI(
    title=f"CTBC - {settings.APP_ENV}",
    description="CTBC Documentation",
    docs_url="/docs" if settings.DOCS is True else None,
    openapi_url="FastAPI Documentation",
    version=settings.APP_VERSION,
    swagger_ui_parameters={
        "persistAuthorization": True,
        "tryItOutEnabled": True,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "X-Internal-User-Email"],
)
app.add_middleware(GZipMiddleware, minimum_size=500)
# include router
app.include_router(main.router)


class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return (
            record.args
            and len(record.args) >= 3
            and record.args[2] not in ["/hc", "/favicon.ico"]
        )


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

