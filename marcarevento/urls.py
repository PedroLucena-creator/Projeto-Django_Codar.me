from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from agenda.urls import urlpatterns as agenda_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('agenda.urls'))
]
