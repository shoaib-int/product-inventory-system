from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://enventory_user:8OVKqsJiY6aAcrfzocNrnLmJ61JF6t34@dpg-d4qt55s9c44c73bjinjg-a.singapore-postgres.render.com/enventory"
engine=create_engine(db_url)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)