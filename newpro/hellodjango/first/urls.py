__author__ = 'Administrator'
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    # path('admin/',admin.site.urls),
    path('index/',views.show_index,name='index'),
    path('',views.show_subject),
    path('teacher/',views.show_teacher),
    path('praise/',views.praise_or_criticize),
    path('criticize/',views.praise_or_criticize),
    path('captcha/',views.get_captcha),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
    path('admin/',admin.site.urls),
]