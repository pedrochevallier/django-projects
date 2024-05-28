from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.url, name='url'),
    path('<str:url>', views.redirect_to_original, name='redirect_to_original'),
]