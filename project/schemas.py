from typing import Any
from pydantic import BaseModel, validator
from pydantic.v1.utils import GetterDict

from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        
        return res
    
class ResponseModel(BaseModel):
    class Config:
        from_attributes = True
        getter_doct = PeeweeGetterDict
            
class UserRequestModel(BaseModel):
    username: str
    password: str
    
    @validator('username')
    def username_valdiator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('Username lenght must be between 3 and 50 characters')
        return username
    
class UserResponseModel(ResponseModel):
    id: int
    username: str

# -------- Movie --------
class MovieResponseModel(ResponseModel):
    id: int
    title: str


# -------- Review --------

class ReviewValidator():
    @validator('score')
    def score_validator(cls, score):
        if score < 1 or score > 5:
            raise ValueError('Score must be between 1 and 5')
        return score
        
class ReviewRequestModel(BaseModel, ReviewValidator):
    user_id: int 
    movie_id: int  
    review: str
    score: int
    
    
class ReviewRequestPutModel(BaseModel, ReviewValidator):  
    review: str
    score: int
        
    
class ReviewResponseModel(ResponseModel): 
    movie: MovieResponseModel
    review: str
    score: int