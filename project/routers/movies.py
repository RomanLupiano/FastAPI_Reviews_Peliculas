from fastapi import APIRouter, HTTPException

from ..database import Movie

from ..schemas import MovieResponseModel, MovieRequestModel

from typing import List

router = APIRouter(prefix='/movies')


@router.get('', response_model=List[MovieResponseModel])
async def get_movies(page: int = 1, limit: int = 10):
    
    if page <= 0 or limit <= 0:
        raise HTTPException(400, 'Params must be greater than zero')
    
    movies = Movie.select().paginate(page, limit)
    
    return [movie for movie in movies]


@router.get('/{movie_id}', response_model=MovieResponseModel)
async def get_movie(movie_id: int = 1):
    
    if movie_id <= 0:
        raise HTTPException(400, 'Params must be greater than zero')
    
    movie = Movie.select().where(Movie.id == movie_id).first()
    
    if movie is None:
        raise HTTPException(404, 'Movie not found')
    
    return movie


@router.post('', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    if Movie.select().where(Movie.title == movie.title).exists():
        raise HTTPException(409, 'Movie already exist')
    
    movie = Movie.create(
        title=movie.title
    )
    
    return movie


@router.put('/{movie_id}', response_model=MovieResponseModel)
async def update_movie(movie_id: int, movie_request: MovieRequestModel):
    if movie_id <= 0:
        raise HTTPException(400, 'Params must be greater than zero')
    
    movie = Movie.select().where(Movie.id == movie_id).first()
    
    if movie is None:
        raise HTTPException(404, 'Movie not found')
    
    movie.title = movie_request.title
    
    movie.save()
    
    return movie


@router.delete('/{movie_id}', response_model=MovieResponseModel)
async def delete_movie(movie_id: int):
    if movie_id <= 0:
        raise HTTPException(400, 'Params must be greater than zero')
    
    movie = Movie.select().where(Movie.id == movie_id).first()
    
    if movie is None:
        raise HTTPException(404, 'Movie not found')
    
    movie.delete_instance()
    
    return movie