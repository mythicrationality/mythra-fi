# coding=utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ota-yhteytta', views.contact, name='contact'),
    path('överit', views.midsummer_redirect, name='midsummer-redirect'),
    path('overit', views.midsummer_redirect, name='midsummer-redirect'),
]
