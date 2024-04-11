from django.urls import path
from .views import CategoryCreate__ListEndPoint,BlogPostList_CreateEndpoint,BlogPostByUserListView,BlogPostDetailEndPoint,BlogPostByCategoryListView

urlpatterns=[
    path('users/create-post/',BlogPostList_CreateEndpoint.as_view(), name='blogpost-create'),
    path('users/update-post/<int:pk>/', BlogPostDetailEndPoint.as_view(), name='blogpost-update'),
    path('users/delete-post/<int:pk>/', BlogPostDetailEndPoint.as_view(), name='blogpost-delete'),
    path('categories/create/', CategoryCreate__ListEndPoint.as_view(), name='category-create'),
    path('posts/category/<int:category_id>/',BlogPostByCategoryListView.as_view(),name='posts-by-category'),
    path('users/retrieve-post/<int:pk>/', BlogPostDetailEndPoint.as_view(), name='post-detail'),
    path('posts/user/<int:user_id>/', BlogPostByUserListView.as_view(), name='posts-by-user'),
    path('users/list-post/', BlogPostList_CreateEndpoint.as_view(), name='blogpost-list'),
    path('categories/list/',CategoryCreate__ListEndPoint.as_view(), name='categories-list')
]
