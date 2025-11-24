from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError
from app.core.auth import verify_access_token


PROTECTED_PATHS = [
    "/api/v1/borrowers",
]


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # Only protect selected routes
        if any(request.url.path.startswith(p) for p in PROTECTED_PATHS):

            auth_header = request.headers.get("Authorization")

            if not auth_header or not auth_header.startswith("Bearer "):
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Missing or invalid Authorization header"},
                )

            token = auth_header.split(" ")[1]

            try:
                payload = verify_access_token(token)
                request.state.user = payload["sub"]
            except JWTError:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Invalid or expired access token"},
                )

        return await call_next(request)
