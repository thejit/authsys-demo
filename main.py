from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from authsys_demo import crud, models, schemas
from authsys_demo.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/ping")
async def ping():
    return {"msg": "pong"}


@app.post("/users/register", status_code=201, response_model=schemas.UserInfo)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="Username already registered")
    return crud.create_user(db=db, user=user)
