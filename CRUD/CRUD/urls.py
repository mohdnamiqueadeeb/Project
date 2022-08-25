
from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('addrecord/', views.addrecord),
    path('deleterecord/<int:num>/', views.deleteRecord),
    path('editrecord/<int:num>/', views.editRecord),
]
