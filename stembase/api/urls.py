from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:resource_id>/', views.resource, name='resource'),
    path('all/', views.all_resource, name='resource'),
]
