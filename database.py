from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://enventory_bm3i_user:JLtV31oFHgQBOrSdnROzb7u8opOzbzaG@dpg-d5l6lce3jp1c739422tg-a.singapore-postgres.render.com/enventory_bm3i"
engine=create_engine(db_url)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)