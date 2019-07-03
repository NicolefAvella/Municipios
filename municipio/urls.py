from django.conf.urls import url, include
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

app_name = "municipio"

urlpatterns = [

    path('', views.municipio_view, name='municipio_view'),
    path('municipio/<int:pk>/', views.municipio_detail, name='municipio_detail'),
    path('municipio/new/', views.municipio_new, name='municipio_new'),
    path('municipio/<int:pk>/edit/', views.municipio_edit, name='municipio_edit'),
    path('municipio/<int:pk>/delete/', views.municipio_delete, name='municipio_delete'),
    path('municipio/<int:pk>/r', views.region_detail, name='region_detail'),
    path('municipio/newr/', views.region_new, name='region_new'),
    path('municipio/<int:pk>/editr/', views.region_edit, name='region_edit'),
    path('municipio/<int:pk>/deleter/', views.region_delete, name='region_delete'),
 ]


