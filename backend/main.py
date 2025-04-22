"""Main module for the AI Story Creator backend FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import settings
from backend.routers import health
from backend.utils.database import create_database_tables


# Initialize FastAPI application
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version=settings.version,
    description="Backend API for AI Story Creator",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.cors_origins],
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

# Include routers
app.include_router(health.router, prefix=settings.api_prefix)


# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize resources when the application starts."""
    # Create database tables (for development)
    if settings.debug:
        await create_database_tables()


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources when the application shuts down."""
    # Placeholder for any cleanup tasks
    pass


if __name__ == "__main__":
    """Run the application directly with Uvicorn if executed as a script."""
    import uvicorn
    uvicorn.run(
        "backend.main:app", 
        host=settings.host, 
        port=settings.port, 
        reload=settings.debug
    )