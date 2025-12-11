from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://postgres:test1234@localhost:5432/fluttermusicapp'
DATABASE_URL = 'postgresql://postgres:neDiQGTXFXcZALmtTrMkyjHeeSzjPuIV@switchback.proxy.rlwy.net:48278/railway'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()