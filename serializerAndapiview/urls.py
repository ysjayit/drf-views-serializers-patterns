from django.urls import path
from .views import PostAPIView, PostDetailAPIView


urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts-list'),
    path('posts/<int:id>/', PostDetailAPIView.as_view(), name='post-detail'),
]
