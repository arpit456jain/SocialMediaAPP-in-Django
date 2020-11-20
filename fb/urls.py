
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('arpit/', views.arpit, name='arpit'),
    path('lite/', views.lite, name='lite'),
    path('messenger/', views.messenger, name='messenger'),
]
