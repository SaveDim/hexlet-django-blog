from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    title = 'Заголовок'
    description = 'Описание'
    created_at = datetime.date.today
    return render(request, 'articles/index.html', context={
        'title': title, 'description': description,
        'created_at': created_at,
    })
