

from django.urls import path
from . import views
from .views import *
from django.contrib import admin


urlpatterns = [
     path('admin/', admin.site.urls),
    path('login', views.login, name='login_api'),
    path('signup',views.signup,name='signup'),
    path('allusers', views.allusers, name='allusers'),
     path('sample', views.sample, name='sample'),
]

