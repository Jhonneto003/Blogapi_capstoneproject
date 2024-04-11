from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BlogPostSerializer,CategorySerializer
from rest_framework.response import Response
from .models import BlogPost,Category
from UserService.models import CustomUser
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.http import Http404


# Create your views here.


class BlogPostByCategoryListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the ucategory ID from the URL parameters
        category_id = self.kwargs.get('category_id')      # Assuming the URL pattern includes 'category_id'
        
        # Check if the category exists
        try:
           category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise Http404("Category does not exist")
        
        return BlogPost.objects.filter(category__id=category_id)


class BlogPostByUserListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    

    def get_queryset(self):
        # Retrieve the user ID and category ID from the URL parameters
        user_id = self.kwargs.get('user_id')  # Assuming the URL pattern includes 'user_id'
      
          # Check if the user exists
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise Http404("User does not exist")


        # Filter blog posts by the specified user ID and category ID
        queryset = BlogPost.objects.filter(author__id=user_id)
        
        return queryset



class BlogPostList_CreateEndpoint(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        return BlogPost.objects.select_related('category').all()



  


   


@method_decorator(csrf_exempt, name='dispatch')   
class BlogPostDetailEndPoint(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
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
        
    


class CategoryCreate__ListEndPoint(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
    

# class CategoryListAPIView(generics.ListAPIView):
    
    