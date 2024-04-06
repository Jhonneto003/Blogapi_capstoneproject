from django.urls import path
from .views import BlogPostCreateView,BlogPostDeleteView,BlogPostUpdateView,CategoryCreateAPIView,BlogPostListAPIView,CategoryListAPIView,BlogPostByCategoryListView,BlogPostByUserListView,BlogPostDetailView

urlpatterns=[
    path('posts/users/create/',BlogPostCreateView.as_view(), name='blogpost-create'),
    path('posts/users/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('posts/users/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
    path('categories/users/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/posts/<int:pk>/',BlogPostByCategoryListView.as_view(),name='posts-by-category'),
    path('posts/detail/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('user/posts/<int:pk>/', BlogPostByUserListView.as_view(), name='posts-by-user'),
    path('posts/', BlogPostListAPIView.as_view(), name='blogpost-list'),
    path('categories/',CategoryListAPIView.as_view(), name='categories-list')
]