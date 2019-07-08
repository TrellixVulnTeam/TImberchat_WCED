
from django.contrib import admin
from django.urls import path, include
from . import views
from api import urls
from website import urls as website_urls
from chat import urls as chat_urls
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(website_urls), name='homepages'),
    path('api/', include(urls)),
    path('chat', include(chat_urls)),
]
