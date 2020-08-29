from django.conf.urls import url

from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from .views import logoutview

urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),

    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(), name="logout"),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('register/requester/', views.requesterView, name='requester_url'),
    path('requester/', views.requesterView, name='requester_url'),
    path('profile/', views.profile, name='profile'),
    path('recipient/', views.recipientView, name='recipient'),

    path('requesterupdate/', views.RequesterUpdate.as_view(), name='requesterupdate'),

    # path(
    #     'login/',
    #     LoginView.as_view(
    #         template_name="login.html",
    #         authentication_form=UserLoginForm
    #         ),
    #     name='login'
    # ),
]
