# main/views.py
from django.shortcuts import render
from .tocurr import calculator_of_currencies
from .currencies import get_currencies_names

currencies = get_currencies_names()

def index(request):
    context = {
        'currencies': currencies
    }
    if request.method == 'POST':
        from_amount = request.POST.get('from_amount')
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')
        result = calculator_of_currencies(from_amount, from_curr, to_curr)
        if result:
            context['result'] = round(result, 2)
            context['from_amount'] = from_amount
            context['from_curr'] = from_curr
            context['to_curr'] = to_curr

    return render(request, 'index.html', context=context)