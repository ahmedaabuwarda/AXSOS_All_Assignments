from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='courses'),
    path('courses/store', views.store, name='courses.store'),
    path('courses/delete/<int:id>', views.delete, name='courses.delete'),
    path('courses/destroy', views.destroy, name='courses.destroy'),
]