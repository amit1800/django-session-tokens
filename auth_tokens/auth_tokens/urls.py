from django.contrib import admin
from django.urls import re_path
from auth_tokens import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test', views.test_token),

]
