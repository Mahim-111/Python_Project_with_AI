from db import engine, Base
from models import User, Report

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")