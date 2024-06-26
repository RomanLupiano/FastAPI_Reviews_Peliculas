from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from project.database import database as connection, User, Movie, UserReview

from .routers import user_router, review_router, movies_router

from .common import create_access_token

app = FastAPI(title='Movie review project in Fast API', version='1')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)
api_v1.include_router(movies_router)

app.include_router(api_v1)

@app.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 

    return {
        'access_token': create_access_token(user.id, user.username),
        'token_type': 'bearer'
    } 


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        print('Connecting to database...')
        
    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Closing database...')



@app.get('/')
async def index():
    return 'Hello World, go to /docs to see the endpoints and make requests'





