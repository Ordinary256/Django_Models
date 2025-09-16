"""
URL configuration for assess project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from anger.views import attendance,home,viewOneStudent,deleteRecord,updatePage,editRecord

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('add/',attendance),
    #dynamic urls
    path('view/<str:record_id>/',viewOneStudent),
    path('delete/<str:record_id>/',deleteRecord),
    path('update/<str:record_id>/',updatePage),
    path('edit/<str:record_id>/',editRecord)
]
