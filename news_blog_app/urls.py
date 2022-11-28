"""news_blog_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('blogs/', include('blog.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),
    # Email with link and reset instructions
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),
    # Final email that lets that user know that password has been reset and they can now login
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
    
]
