from fastapi import HTTPException, APIRouter

from ..database import User

from ..schemas import UserResponseModel, UserRequestModel

router = APIRouter(prefix='/users')

@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409, 'Username already in use, please enter another username')
    
    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )
    
    return user