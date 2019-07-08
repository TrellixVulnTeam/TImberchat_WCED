from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.Chat.as_view(), login_url='/login'), name= "chat_index"),
]