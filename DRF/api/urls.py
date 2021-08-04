from django.contrib import admin
from django.urls import path,include
app_name = 'api'
from .views import artlist,artdet ,Userlist,Userdet,cat
urlpatterns = [
    path('',artlist.as_view(),name = 'list'),
    path('<slug:slug>',artdet.as_view(),name = 'det'),
    path('user/',Userlist.as_view(),name = 'list'),
    path('user/<int:pk>',Userdet.as_view(),name = 'det'),
    path('category/<slug:slug_cat>',cat,name = 'cat'),
]