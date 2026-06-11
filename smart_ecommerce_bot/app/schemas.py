from pydantic import BaseModel


class QueryRequest(BaseModel):
    session_id: str
    user_query: str


class ClearRequest(BaseModel):
    session_id: str
