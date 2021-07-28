from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# 메서드 안에다가 직접 사용하지 못하기 때문에
# 함수에 들어가는 메소드를 변환해주기 위함
# get, 방식과 post 방식에 적용

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('acountapp:hw')
    template_name = 'profileapp/create.html'

    # 유저 직접할당
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# 나만 수정해야하므로, 커스텀 데꼬레이션 만들어줌
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    # 어떤 것을 입력받아 수정할건지
    form_class = ProfileCreationForm
    # HTML에서 불러오는 이름
    context_object_name = 'target_profile'
    # 업데이트 후 어디로 갈지 정해줌
    success_url = reverse_lazy('acountapp:hw')
    # 어떤 템플릿에서 사용할지 정해줌
    template_name = 'profileapp/update.html'
