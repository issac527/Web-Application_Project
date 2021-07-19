from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from acountapp.forms import AccountCreationForm
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

def hello_world(request):
    # 요청을 보내는 유저가 로그인이 되어있다면 아래 구문 실행
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse("acountapp:login"))

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

# 비회원들한테는 보여지면 안됨
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:hw')
    template_name = 'acountapp/update.html'

    def get(self, request, *agrs, **kwargs):
        # 유저가 로그인되어 있다면 부모 클래스 실행
        if request.user.is_authenticated:
            return super().get(request, *agrs, **kwargs)
        else:
            return HttpResponseRedirect(reverse("acountapp:login"))

    def post(self, request, *args, **kwargs):
        # 유저가 로그인되어 있다면 부모 클래스 실행
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("acountapp:login"))


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("acountapp:hw")
    template_name = 'acountapp/delete.html'

    def get(self, request, *agrs, **kwargs):
        # 유저가 로그인되어 있다면 부모 클래스 실행
        if request.user.is_authenticated:
            return super().get(request, *agrs, **kwargs)
        else:
            return HttpResponseRedirect(reverse("acountapp:login"))

    def post(self, request, *args, **kwargs):
        # 유저가 로그인되어 있다면 부모 클래스 실행
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("acountapp:login"))