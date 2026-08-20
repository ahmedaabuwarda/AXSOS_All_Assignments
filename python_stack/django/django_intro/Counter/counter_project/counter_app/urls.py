from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('increment', views.increment, name='increment'),
    path('incrementByTwo', views.incrementByTwo, name='incrementByTwo'),
    path('destroy_session', views.destroy_session, name='destroy_session')
]