from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CommentArticleForm

from hexlet_django_blog.article.models import Article

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form}) # Передаем нашу форму в контексте


# class CommentArticleView(View):
#
#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
#         if form.is_valid(): # Проверяем данные формы на корректность
#             comment = Comment(
#                 name = form.cleaned_data['content'], # Получаем очищенные данные из поля content
#                         # Заполняем оставшиеся поля
#                 )
#             comment.save()


# class ArticleCommentsView(View):
#
#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
#         return render(request, 'articles/show.html', context={
#             'Comment': Comment,
#         }))