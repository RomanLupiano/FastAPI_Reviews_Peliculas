from fastapi import FastAPI, APIRouter

from project.database import database as connection, User, Movie, UserReview

from .routers import user_router, review_router

app = FastAPI(title='Movie review proyect in Fast API', version='1')

api_v1 = APIRouter(prefix='/api/v1')
api_v1.include_router(user_router)
api_v1.include_router(review_router)

app.include_router(api_v1)


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





