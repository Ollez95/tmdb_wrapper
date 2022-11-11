from abc import ABC, abstractmethod
from typing import Any, Dict

from tmdb_wrapper.tmdb.parse import ParseData

from pprint import pprint

class Datatype(ABC):
    '''
    Abstract Class to get different requests
    '''
    @abstractmethod
    def to_datatype(
        self,
        parse_data : ParseData = None,
        model_data : Any = None,
        custom_model: Any = None):
        '''
        This method returns the type of data you want to receive from the request.

        :class ModelDatatype: returns the data model by default tested by the owner of the project.
        :class CustomModelDatatype: returns the data model customized by the user.
        :class DictionaryDatatype: returns the data model in a dictionary data structure.
        :class PrettifyDatatype: prints the parsed data in a prettify way.
        :class OriginalDatatype: returns the original data.

        example:
        def movie_certifications(self):
 
            certifications = Certifications()

            response = certifications.get_movie_certifications(
                datatype = PrettifyDatatype()
            )

        '''
        

class ModelDatatype(Datatype):
    '''
    Default Model Datatype Tested
    '''
    def to_datatype(
        self,
        parse_data : ParseData = None,
        model_data : Any = None,
        custom_model: Any = None) -> Any:
        return parse_data.to_data(class_type = model_data)

class CustomModelDatatype(Datatype):
    '''
    Custom data model
    '''
    def to_datatype(
        self,
        parse_data : ParseData = None,
        model_data : Any = None,
        custom_model: Any = None) -> Any:
        return parse_data.to_data(class_type = custom_model)

class DictionaryDatatype(Datatype):
    '''
    Dictionary data model
    '''
    def to_datatype(
        self,
        parse_data : ParseData = None,
        model_data : Any = None,
        custom_model: Any = None) -> Dict:
        return dict(parse_data)

class PrettifyDatatype(Datatype):
    '''
    Prettify data
    '''
    def to_datatype(
        self,
        parse_data : ParseData = None,
        model_data : Any = None,
        custom_model: Any = None) -> Dict:
        pprint(dict(parse_data))

class OriginalDatatype(Datatype):
    '''
    Original data model
    '''
    def to_datatype(
        self,
        parse_data : ParseData = None,
        model_data : Any = None,
        custom_model: Any = None) -> Dict:
        return parse_data
