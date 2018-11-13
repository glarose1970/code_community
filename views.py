from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': 'Now I am from first_app/index.html',
               't_one': 'added from views.py',
               't_two': 'second insert',
               't_three': 'third insert into table', }
    return render(request, 'first_app/index.html', context=my_dict)
