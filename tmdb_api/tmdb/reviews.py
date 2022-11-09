import textwrap
from typing import Any
from tmdb_api.data.movie import ModelMovies
from tmdb_api.data.review import Review
from tmdb_api.tmdb.base import TMDb
from tmdb_api.tmdb.datatype import Datatype, ModelDatatype
from tmdb_api.tmdb.excep import TMDbException
from tmdb_api.tmdb.request import  GetRequest

class Reviews(TMDb):
    '''
    Trendings Class
    '''
    def get_reviews(
        self,
        datatype : Datatype = ModelDatatype(),
        review_id: str = None) -> Any:

        '''
        Retrieve the details of a movie or TV show review.


        See more: https://developers.themoviedb.org/3/trending/get-trending
        '''


        parse_data = self.request_data(
            request_operation = GetRequest(),
            path = f"/review/{review_id}")

        return datatype.to_datatype(parse_data = parse_data, model_data = Review)