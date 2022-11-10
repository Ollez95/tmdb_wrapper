import pickle
from datetime import datetime
from typing import Callable

from tmdb_wrapper.tmdb.request import Request


def read_pickle(route: str) -> dict:
    '''
    load pickle file
    '''
    with open(route, 'rb') as read:
        dct = pickle.load(read)

    return dct, compare_dates(dct['expires_at'])

def save_pickle(data: dict, route: str) -> pickle:
    '''
    save pickle file
    '''
    with open(route, 'wb') as write:
        pickle.dump(data, write)


def compare_dates(date_file: str) -> bool:
    '''
    Compare 2 dates, convert them to datetime format and return a boolean.

    date_file : str
        date that belongs to expire session id.
    '''
    date_file_to_date = datetime.strptime(date_file, "%Y-%m-%d %H:%M:%S UTC")
    today_to_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today_to_date = datetime.strptime(today_to_str, "%Y-%m-%d %H:%M:%S")
    return date_file_to_date > today_to_date

def init_session_type(
    request_data: Callable,
    request_operation: Request,
    path: str,
    **kwargs):
    '''
    init user or guest type session
    '''
    return request_data(
        request_operation = request_operation,
        path = path,
        **kwargs)