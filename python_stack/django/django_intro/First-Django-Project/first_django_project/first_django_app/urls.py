from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:blog_id>', views.show),
    path('blogs/<int:blog_id>/edit', views.edit),
    path('blogs/<int:blog_id>/delete', views.destroy),
    path('blogs/json', views.json),
]