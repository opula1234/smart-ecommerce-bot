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

nest_asyncio.apply()


# Database configuration
DATABASE_URL = "sqlite:///electronic_store.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    SQLModel.metadata.create_all(engine)

    yield

    # Shutdown logic (optional)
    print("Application shutting down...")

app = FastAPI(
    title="Smart E-Commerce Sales Bot (RAG)",
    lifespan=lifespan,
    description="AI-powered sales assistant for Machi Electronics with conversation memory."
)


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    brand: str
    price: float
    specs: str
    stock: int = Field(default=10)  # Stock Availability
