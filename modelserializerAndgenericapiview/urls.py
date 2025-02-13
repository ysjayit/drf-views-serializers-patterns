from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:id>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]