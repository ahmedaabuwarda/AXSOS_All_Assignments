from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='shows.root'),
    path('shows', views.index, name='shows.index'),
    path('shows/create', views.create, name='shows.create'),
    path('shows/store', views.store, name='shows.store'),
    path('shows/<int:id>/edit', views.edit, name='shows.edit'),
    path('shows/update', views.update, name='shows.update'),
    path('shows/<int:id>', views.show, name='shows.show'),
    path('shows/<int:id>/delete', views.delete, name='shows.delete'),
]