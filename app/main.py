from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import categories, imports, summary, transactions, rules
from app.models import categorization_rules, category, import_log, transaction
from app.core.database import Base, engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,           
    allow_methods=["*"],              
    allow_headers=["*"],              
)

app.include_router(
    categories.router,
    prefix="/api"
                   )

app.include_router(
    imports.router,
    prefix="/api"
                   )

app.include_router(
    summary.router,
    prefix="/api"
                   )

app.include_router(
    transactions.router,
    prefix="/api"
                   )

app.include_router(
    rules.router,
    prefix="/api"
                   )

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
