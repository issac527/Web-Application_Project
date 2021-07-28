from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profile'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name="create"),
    # pk라는 int 타입의 데이터를 넘겨 받는다
    path('update/<int:pk>', ProfileUpdateView.as_view(), name="update"),
]