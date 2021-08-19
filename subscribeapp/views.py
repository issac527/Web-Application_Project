from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription
from django.urls import reverse

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):

        # 어떤 유저가 이 버튼을 눌렀는지, 어떤 게시물에 구독 버튼을 눌렀는지 확인해야 함
        user = request.user
        # 주소창으로 넘겨받는 pk를 받음
        project = Project.objects.get(pk=kwargs['project_pk'])

        # 두 가지의 조건을 만족하는 데이터를 찾아냄
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        # 조건 만족 시 구독 해지
        if subscription.exists():
            subscription.delete()
        # 구독 정보가 존재하지 않을 시 구독
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    # 요청 처리 후 어디로 갈지 설정
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':kwargs['project_pk']})