from django.shortcuts import render


def index(request):
    articles = ['1', '2', '3']
    return render(
        request,
        'articles.html',
        context={'articles': articles},
    )
