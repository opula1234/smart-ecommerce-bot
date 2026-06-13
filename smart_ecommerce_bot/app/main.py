import os
import uvicorn
import nest_asyncio
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select
from langchain_google_genai import ChatGoogleGenerativeAI
from collections import defaultdict
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from app.routers import sales_bot
from app.seed_data import seed_products
# Import models to ensure they are registered in SQLModel.metadata
from app.models import Product


nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()


# Database configuration
DATABASE_URL = "sqlite:///electronic_store.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    SQLModel.metadata.create_all(engine)

    # Seed the database
    with Session(engine) as session:
        seed_products(session)

    # Initialize AI model and conversation memory
    app.state.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    app.state.conversation_store = defaultdict(list)

    yield

    # Shutdown logic (optional)
    print("Application shutting down...")
    app.state.conversation_store.clear()

app = FastAPI(
    title="Smart E-Commerce Sales Bot (RAG)",
    lifespan=lifespan,
    description="AI-powered sales assistant for Machi Electronics with conversation memory."
)


# Include the sales bot router
app.include_router(sales_bot.router)


@app.get("/")
async def root():
    return {"message": "Sales Bot Running"}
