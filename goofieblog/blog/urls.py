from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', postslist.as_view(), name='home'),
    path('', views.postslist.as_view(),name='posts'),
    path('<slug:slug>/',views.postdetail.as_view(),name='post_detail'),
    path('<slug:slug>/amp/', post_detail_amp, name='post_detail_amp'),
]