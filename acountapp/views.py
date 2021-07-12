from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.views.generic import CreateView

# Create your views here.
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy


def hello_world(request):
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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm()
    # 클래스 내에서 reverse시 reverse_lazy로 사용
    success_url = reverse_lazy("acountapp:hw")
    template_name = "accountapp/create.html"
