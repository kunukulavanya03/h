from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.dependencies import get_db, oauth2_scheme
from app.utils import authenticate_user, create_access_token

router = APIRouter(
    prefix='/api/auth',
    tags=['auth'],
)

@router.post('/register')
def create_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if user:
        raise HTTPException(status_code=400, detail='Username already exists')
    new_user = User(username=form_data.username, email=form_data.username, password=form_data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'token': create_access_token(data={'sub': new_user.username})}

@router.post('/login')
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid username or password')
    return {'token': create_access_token(data={'sub': user.username})}