from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('seed', views.seed),
    path('thank_you', views.thank_you)
]
