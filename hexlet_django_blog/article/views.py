from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        title = 'Заголовок'
        description = 'Описание'
        created_at = datetime.date.today
        return render(request, 'articles/index.html', context={
            'title': title, 'description': description,
            'created_at': created_at,
        })
