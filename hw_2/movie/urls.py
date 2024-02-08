from django.contrib import admin
from django.urls import path

from .views import get_ingex_page

urlpatterns = [
    path('', get_ingex_page),

]