from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from acountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get("hwt")
        n_hw = HelloWorld()
        n_hw.text = temp
        n_hw.save()
        HelloWorld_list = HelloWorld.objects.all()

        return render(request, 'acountapp/hello_world.html',
                      context={"HelloWorld_list": HelloWorld_list})
    else:
        HelloWorld_list = HelloWorld.objects.all()
        return render(request, 'acountapp/hello_world.html',
                      context={"HelloWorld_list": HelloWorld_list})