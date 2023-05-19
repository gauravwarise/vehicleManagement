from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.index),
    path('create',v.create),
    path('register',v.register),
    path('signin',v.loginn),
    path('signout',v.logoutt),
    path('retrieve',v.retrieve),
    path('change/<int:id>',v.update),
    path('delete/<int:id>',v.delete)
]