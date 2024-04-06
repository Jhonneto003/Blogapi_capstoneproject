from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BlogPostSerializer,CategorySerializer
from rest_framework.response import Response
from .models import BlogPost,Category
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator


# Create your views here.

class BlogPostByUserListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # Retrieve the user ID from the URL parameter
        user_id = self.kwargs['pk']
        # Filter blog posts by the specified user
        queryset = BlogPost.objects.filter(author__id=user_id)
        return queryset
    


class BlogPostByCategoryListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # Retrieve the category ID from the URL parameter
        category_id = self.kwargs['pk']
        # Filter blog posts by the specified category
        queryset = BlogPost.objects.filter(category__id=category_id)
        return queryset

class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.select_related('category').all()

@method_decorator(csrf_exempt, name='dispatch')
class BlogPostUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        # Check if the user is the author of the blog post
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        return obj



@method_decorator(csrf_exempt, name='dispatch')
class BlogPostDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [TokenAuthentication]


    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        # Check if the user is the author of the blog post
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        return obj
    
class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    


class CategoryCreateAPIView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication]


    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer