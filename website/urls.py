from django.urls import path, include
from . import views
from api import urls

urlpatterns = [
    path('', views.HomePage.as_view(), name='website_homepage'),
    path('login', views.Login.as_view(), name='website_login'),
    path('registration', views.Registration.as_view(), name='website_register'),
]
