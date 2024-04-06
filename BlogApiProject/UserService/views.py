# from django.shortcuts import render
# from .serializers import CustomUserSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate

# # Create your views here.

# class SignUp(APIView):
#     def post(self,request,*args, **kwargs):
#         incoming_data=request.data
#         serializer=CustomUserSerializer(data=incoming_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class Login(APIView):
#     def post(self,request,*args, **kwargs):
#         username_or_email= request.data.get('username_or_email')
#         password = request.data.get('password')

#         user=authenticate(username=username_or_email, password=password)
#         if user:
#             token=Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import CustomUserSerializer
from rest_framework import status,exceptions



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        user = request.user
        serialized_user = CustomUserSerializer(user).data
        if request.user.is_authenticated:
            return Response(serialized_user, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)




