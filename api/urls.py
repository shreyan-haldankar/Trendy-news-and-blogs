from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView

urlpatterns = [
    # View existing blog lists
    path('', PostListView.as_view(),name="listcreate"),
    # Perform CRUD operations on blogs
    path('<str:pk>', PostDetailView.as_view(), name="detailcreate")    
]