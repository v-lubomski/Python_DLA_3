from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def hello_url(request):
    return HttpResponse("Hello url!")


def hello_path(request):
    return HttpResponse("Hello path!")

