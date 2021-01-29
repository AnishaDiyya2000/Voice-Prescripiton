"""voice_prescription URL Configuration

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
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),

    path('doctors/login/', views.doctor_login, name='doc_login'),
    path('doctors/logout/', views.m_logout, name='doc_logout'),
    path('doctors/registration/', views.doctor_registration,
         name='doctor_registration'),

    path('doc_navbar', views.doc_navbar, name='doc_navbar'),
    path('voice_p', views.voice_p, name='voice_p'),
    # path('admin_base', views.admin_base, name='admin_base'),
    path('addAndShow', views.addAndShow, name='addAndShow'),
    path('delete/<int:id>/', views.delete_data, name='deleteData'),
    path('<int:id>/', views.updateDoc, name='updateDoc')
]
