from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from django.views.generic.list import MultipleObjectMixin

from acountapp.decorators import account_ownership_required
from acountapp.forms import AccountCreationForm
from acountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

from articleapp.models import Article

has_ownership = [login_required, account_ownership_required]


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
    #success_url = reverse_lazy("acountapp:login")
    template_name = "acountapp/create.html"

    def get_success_url(self):
        return reverse("acountapp:detail", kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = "acountapp/detail.html"

    paginate_by = 20

    def get_context_data(self, **kwargs):
        # 현재 접속된 유저의 Article 데이터를 필터링하여 article_list에 넣어줌
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    #success_url = reverse_lazy('acountapp:hw')
    template_name = 'acountapp/update.html'

    def get_success_url(self):
        return reverse("acountapp:detail", kwargs={'pk': self.object.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("acountapp:hw")
    template_name = 'acountapp/delete.html'
