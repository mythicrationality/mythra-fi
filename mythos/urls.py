# coding=utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ota-yhteytta/', views.contact, name='contact'),
    path('johdanto/kaj/', views.introduction_kaj, name='introduction-kaj'),
    path('johdanto/lumi/', views.introduction_lumi, name='introduction-lumi'),
    path('överit/', views.midsummer_redirect, name='midsummer-redirect'),
    path('overit/', views.midsummer_redirect, name='midsummer-redirect'),
]
