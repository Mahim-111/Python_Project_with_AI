from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = {
    "url": os.getenv("URLDB")
}


engine = create_engine(
    DATABASE_URL["url"],
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl":True
        }
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()