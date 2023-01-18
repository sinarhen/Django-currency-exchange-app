import requests
from os import environ


def get_currencies():
    response = requests.get(environ['API_KEY']).json()
    return response

def get_currencies_names():
    return [i for i in get_currencies()['data']]

def get_exact_currency_information(name='EUR'):
    return get_currencies()['data'][name]
