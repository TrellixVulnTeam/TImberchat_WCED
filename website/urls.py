from django.urls import path, include
from . import views
from api import urls
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomePage.as_view(), login_url='/login'), name='website_homepage'),
    path('login', views.Login.as_view(), name='website_login'),
    path('logout', login_required(views.Logout.as_view(), login_url='/login'), name='website_logout'),
    path('registration', views.Registration.as_view(), name='website_register'),
]
