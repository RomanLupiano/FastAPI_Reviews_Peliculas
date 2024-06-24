from fastapi import FastAPI, HTTPException

from database import database as connection, User, Movie, UserReview

from schemas import UserRequestModel, UserResponseModel, ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel

from typing import List

app = FastAPI(title='Movie review proyect in Fast API', version='1')

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


@app.post('/users/create', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409, 'Username already in use, please enter another username')
    
    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )
    
    return user


@app.post('/reviews/create', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):

    if (User.select().where(User.id == user_review.user_id).first()) is None:
        raise HTTPException(404, 'User not found')
    
    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(404, 'Movie not found')

    
    user_review = UserReview.create(
        user_id=user_review.user_id,
        movie_id=user_review.movie_id,
        review=user_review.review,
        score=user_review.score
    )
    
    return user_review


@app.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10):
   
    if page <= 0 or limit <= 0:
        raise HTTPException(400, 'Params must be greater than zero')
    
    reviews = UserReview.select().paginate(page, limit)
    
    return [ review for review in reviews]


@app.get('/reviews/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
    review = UserReview.select().where(UserReview.id == review_id).first()
    
    if review is None:
        raise HTTPException(404, 'Review not found')
    
    return review


@app.put('/reviews/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, review_request: ReviewRequestPutModel):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    
    if user_review is None:
        raise HTTPException(404, 'Review not found')
    
    user_review.review = review_request.review
    user_review.score = review_request.score
    
    user_review.save()
    
    return user_review


@app.delete('/reviews/{review_id}', response_model=ReviewResponseModel)
async def delete_review(review_id: int):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    
    if user_review is None:
        raise HTTPException(404, 'Review not found')
    
    user_review.delete_instance()
        
    return user_review