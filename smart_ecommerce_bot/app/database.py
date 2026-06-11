from sqlmodel import create_engine

DATABASE_URL = "sqlite:///electronic_store.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)
