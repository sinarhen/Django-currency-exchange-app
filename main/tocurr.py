from .currencies import get_exact_currency_information

error = ''
def calculator_of_currencies(from_amount, from_curr, to_curr):
    global error
    if not from_amount or int(from_amount)<0:
        error = 'Amount not given or less than 0'
    elif not from_curr:
        error = 'from_curr attribute not given'
    elif not to_curr:
        error = 'to_curr value not given'
    if error:
        raise AttributeError(error)
    return get_exact_currency_information(to_curr) / get_exact_currency_information(from_curr) * float(from_amount)
