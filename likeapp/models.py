from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like_record', null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record', null=False)

    class Meta:
        # 필드가 아닌 모든것 -> Meta
        # ex) 이미지 사이즈, 용량, 날짜 등
        unique_together = ['user', 'article']