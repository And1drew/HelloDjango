from django.urls import path
from helloDjangoApp import views

urlpatterns = [
    path('', views.index_view),
]
