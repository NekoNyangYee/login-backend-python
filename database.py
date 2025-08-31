from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# 사용자명과 비밀번호를 실제 값으로 변경하세요.
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1111@localhost:3306/my_login_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
