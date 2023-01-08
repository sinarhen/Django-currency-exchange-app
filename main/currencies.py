import requests
from os import getenv
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def get_currencies():
    response = requests.get(
        getenv('api_key')
        ).json()
    return response

def get_currencies_names():
    return [i for i in get_currencies()['data']]

def get_exact_currency_information(name='EUR'):
    return get_currencies()['data'][name]
