from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    # 어느 게시판에 구독정보를 보낼건지 설정
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe')
]