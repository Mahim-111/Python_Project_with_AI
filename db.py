from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE_URL = {
#     "url": os.getenv("URLDB")
    
# }
DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:4000/"
    f"{os.getenv('DB_NAME')}"
)


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
