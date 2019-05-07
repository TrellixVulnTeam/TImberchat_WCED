
from django.contrib import admin
from django.urls import path, include
from . import views
from api import urls
from website import urls as website_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(website_urls)),
    path('api/', include(urls))
]
