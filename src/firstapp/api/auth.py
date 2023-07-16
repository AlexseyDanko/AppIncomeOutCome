from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.auth import (
    User,
    UserCreate,
    Token,

)
from ..services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
)


@router.post('/sing-up', response_model=Token)
async def sing_up(
        user_data: UserCreate,
        service: AuthService = Depends(),
):
    return service.register_new_user(user_data)


@router.post('/sing-in', response_model=Token)
async def sing_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends(),
):
    return service.authenticate_user(
        form_data.username,
        form_data.password,
    )


@router.get('/user', response_model=User)
async def get_user(user: User = Depends(get_current_user)):
    return user
