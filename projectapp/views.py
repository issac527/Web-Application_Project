from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from django.urls import reverse

from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        # 구독 정보 여부 확인
        user = self.request.user
        project = self.object

        # 유저가 로그인되어 있지 않다면 None 값 출력
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)
        else:
            subscription = None

        # 해당 프로젝트인 게시글들만 추려내서 article_list에 넘겨줌
        article_list = Article.objects.filter(project=self.object)
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20