from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('hello_path/', views.hello_path),
    url(r'^hello_url/', views.hello_url),
]
