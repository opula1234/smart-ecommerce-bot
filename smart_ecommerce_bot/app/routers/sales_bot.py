import re

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request

from sqlmodel import Session
from sqlmodel import select

from app.models import Product
from app.schemas import QueryRequest
from app.schemas import ClearRequest
from app.dependencies import get_session

router = APIRouter(
    prefix="/api/v1",
    tags=["Sales Bot"]
)


def parse_query_filters(query: str):

    q = query.lower()

    category = None
    budget = None
    brand = None

    categories = {
        "laptop": ["laptop", "notebook", "macbook"],
        "mobile": ["mobile", "phone", "iphone"],
        "tablet": ["tablet", "ipad"],
        "headphones": ["headphones", "earbuds"],
        "smartwatch": ["watch", "smartwatch"],
    }

    for cat, keywords in categories.items():
        if any(word in q for word in keywords):
            category = cat
            break

    k_match = re.search(r"(\d+)\s*k", q)
    num_match = re.search(r"\b(\d{4,6})\b", q)

    if k_match:
        budget = int(k_match.group(1)) * 1000
    elif num_match:
        budget = int(num_match.group(1))

    brands = [
        "apple",
        "samsung",
        "lenovo",
        "asus",
        "hp",
        "dell",
        "acer",
    ]

    for b in brands:
        if b in q:
            brand = b.capitalize()
            break

    return category, budget, brand


@router.post("/sales-bot")
async def sales_bot_handler(
    payload: QueryRequest,
    request: Request,
    session: Session = Depends(get_session),
):

    llm = request.app.state.llm
    conversation_store = request.app.state.conversation_store

    category, budget, brand = parse_query_filters(
        payload.user_query
    )

    statement = select(Product)

    if category:
        statement = statement.where(
            Product.category == category
        )

    if budget:
        statement = statement.where(
            Product.price <= budget
        )

    if brand:
        statement = statement.where(
            Product.brand == brand
        )

    products = session.exec(statement).all()

    context = "\n".join(
        [
            f"{p.name} | ₹{p.price}"
            for p in products
        ]
    )

    history = conversation_store[payload.session_id]

    prompt = f"""
You are a sales expert.

Inventory:
{context}

Conversation:
{history}

Customer:
{payload.user_query}
"""

    response = llm.invoke(prompt)

    history.append(
        {
            "role": "user",
            "content": payload.user_query
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    return {
        "reply": response.content
    }


@router.delete("/sales-bot/clear")
async def clear_chat(
    payload: ClearRequest,
    request: Request
):

    store = request.app.state.conversation_store

    if payload.session_id in store:
        del store[payload.session_id]

    return {
        "message": "Conversation cleared"
    }
