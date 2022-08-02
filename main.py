from fastapi import FastAPI

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

# This will create our database if it doesent already exists
Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
