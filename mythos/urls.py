# coding=utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ota-yhteytta/', views.contact, name='contact'),
    path('johdanto/', views.introduction_index, name='introduction-index'),
    path('johdanto/toukokuu/', views.introduction_king_may, name='introduction-king-may'),
    path('johdanto/lumi/', views.introduction_lumi, name='introduction-lumi'),
    path('johdanto/tiina/', views.introduction_tiina, name='introduction-tiina'),
    path('materiaalit/', views.material_index, name='material-index'),
    path('överit/', views.midsummer_redirect, name='midsummer-redirect'),
    path('overit/', views.midsummer_redirect, name='midsummer-redirect'),
    path('turkuheinäkuu2018/', views.july_redirect, name='midsummer-redirect'),
    path('turkuheinakuu2018/', views.july_redirect, name='midsummer-redirect'),
]
