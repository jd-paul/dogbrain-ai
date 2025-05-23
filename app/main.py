from fastapi import FastAPI
from app.routes import dogcoach, simplifier, smartnudge

app = FastAPI()

# Add all routers here
app.include_router(dogcoach.router)
app.include_router(simplifier.router)
app.include_router(smartnudge.router)
