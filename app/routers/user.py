from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
     prefix="/users",
     tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_posts(user: schemas.User, db: Session = Depends(get_db)):
       
       #has the password user.password
       hashed_password = utils.hash_password(user.password)
       user.password = hashed_password

       create_users = models.User(**user.model_dump())
        
       db.add(create_users)
       db.commit()
       db.refresh(create_users)
       
       return create_users

@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):


    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return user