from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE

from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True) # 연결하는 이름 (User.article) << 이런식으로
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null = True)
    created_at = models.DateField(auto_now_add=True) # 객체 생성 시 그 시간으로 자동 할당

    # 좋아요 필드
    like = models.IntegerField(default=0)