""" Defines URL schemes for users  """
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import login

from . import views as auth_views

from django.contrib.auth.views import LoginView

urlpatterns = [
    # log in page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # log out from page
    path('logout/', auth_views.logout_view, name='logout'),
    # registration
    path('register/', auth_views.register, name='register'),
]


