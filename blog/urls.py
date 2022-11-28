from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name="blogs"),  # root domain
    path('blog/<str:pk>/', views.blog, name="blog"),
    path('create-blog/', views.createBlog, name="create-blog"),
    path('update-blog/<str:pk>/', views.updateBlog, name = "update-blog"),
    path('delete-blog/<str:pk>/', views.deleteBlog, name = "delete-blog"),
]