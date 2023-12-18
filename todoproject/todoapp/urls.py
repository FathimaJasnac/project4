from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklv.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdv.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskuv.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdltv.as_view(),name='cbvdelete'),
]
