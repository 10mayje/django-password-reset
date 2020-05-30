from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    # path('reset-pass', views.reset_password, name='password_reset'),
]
