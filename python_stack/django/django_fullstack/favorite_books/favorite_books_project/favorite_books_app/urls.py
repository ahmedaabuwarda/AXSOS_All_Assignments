from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('books', views.books),
    path('books/store', views.store),
    path('books/update/<int:book_id>', views.update, name='books.update'),
    path('books/<int:book_id>', views.show, name='books.show'),
    path('books/<int:book_id>/add_favorite', views.add_favorite, name='books.add_favorite'),
    path('books/<int:book_id>/remove_favorite', views.remove_favorite, name='books.remove_favorite'),
]