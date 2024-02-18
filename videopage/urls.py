from django.contrib import admin
from django.urls import path
from videoapp.views import videopage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', videopage, name='videopage'),
]
