from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from acountapp.forms import AccountCreationForm
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy


@login_required(login_url=reverse_lazy('acountapp:login'))
def hello_world(request):
    # 요청을 보내는 유저가 로그인이 되어있다면 아래 구문 실행
    if request.method == 'POST':

        temp = request.POST.get("hwt")
        n_hw = HelloWorld()
        n_hw.text = temp
        n_hw.save()

        # 앱기반 라우팅 가능 (url을 직접 적어주지 않고 사용)
        # 이름을 기반으로 주소로 변환해주는(역추적) 함수 사용
        return HttpResponseRedirect(reverse("acountapp:hw"))

        # HttpResponseRedirect를 통해 재연결을 해줄거임
        # return render(request, 'acountapp/hello_world.html',
        #               context={"HelloWorld_list": HelloWorld_list})
    else:
        HelloWorld_list = HelloWorld.objects.all()
        return render(request, 'acountapp/hello_world.html',
                      context={"HelloWorld_list": HelloWorld_list})


# 누구든 갈 수 있어야 함
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # 클래스 내에서 reverse시 reverse_lazy로 사용
    success_url = reverse_lazy("acountapp:login")
    template_name = "acountapp/create.html"


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = "acountapp/detail.html"


# 로그인 사용자 맞는지 확인해줌
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:hw')
    template_name = 'acountapp/update.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("acountapp:hw")
    template_name = 'acountapp/delete.html'