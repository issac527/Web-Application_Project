# 게시글의 작성자와 현재 접속하려는 유저가 동일한지 확인해주는 거얌

from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])  # 단일 객체를 가지고 올거임(pk는 kwargs에 있음)
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated
