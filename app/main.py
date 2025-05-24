from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import dogcoach, simplifier, smartnudge

app = FastAPI()

# Enable CORS so Next.js can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:3000"] in dev if you want to be strict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(dogcoach.router)
app.include_router(simplifier.router)
app.include_router(smartnudge.router)
