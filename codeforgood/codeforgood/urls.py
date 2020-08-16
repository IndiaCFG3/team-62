"""codeforgood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.contrib.auth import views as auth_views
import teacher.views as teacher_views
import principal.views as principal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',auth_views.LoginView.as_view(template_name="teacher/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="teacher/logout.html"),name='logout'),
    path('teacher/home',teacher_views.home,name='teacher-home'),
    path('principal/home',principal_views.home,name='principal-home'),

    path('teacher/<int:id>',principal_views.studentbyTeacher,name='principal-teacher'),
    path('teacher/form/<int:id>',principal_views.studentForm,name='student-form'),

    path('redirectingurl',teacher_views.redirectingview,name='redirectingurl'),

    
    path('teacher/student/<int:id>/',teacher_views.show_questions,name='show_questions'),

    path('changepassword',teacher_views.change_password,name="changepassword"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='course/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='course/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='course/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='course/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
