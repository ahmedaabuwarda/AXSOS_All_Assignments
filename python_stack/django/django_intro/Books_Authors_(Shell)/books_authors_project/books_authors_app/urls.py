from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_author', views.add_author),
    path('add_book', views.add_book),
    path('add_author_to_book', views.add_author_to_book),
    path('add_book_to_author', views.add_book_to_author),
    path('book/<int:book_id>', views.show_book),
    path('author/<int:author_id>', views.show_author),
]
