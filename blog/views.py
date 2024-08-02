from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from blog.models import AllBlog
from blog.serializers import BlogSerializer, RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

def index(request):
  return render(request, "blog/index.html")


class RegisterView(APIView):
  def post(self, request):
    serial_register=RegisterSerializer(data=request.data)
    if serial_register.is_valid():
      serial_register.save()
      user=authenticate(
        username=serial_register.data["username"],
        password=serial_register.data["password"]
      )
      token, _=Token.objects.get_or_create(user=user)
      return Response({
        "status": status.HTTP_201_CREATED,
        "message": "Successfully Registered! ",
        "token": str(token)
      })
    return Response({
      "status": status.HTTP_400_BAD_REQUEST,
      "message": "Incomplete Credentials",
      "body": serial_register.errors
    })


class LoginView(APIView):
  def post(self, request):
    login_serial=LoginSerializer(data=request.data)
    if login_serial.is_valid():
      user=authenticate(
        username=login_serial.data["username"],
        password=login_serial.data["password"]
      )
      if not user:
        return Response({
          "status": status.HTTP_400_BAD_REQUEST,
          "message": "user does not exist !",
          "body": login_serial.errors
        })
      token, _= Token.objects.get_or_create(user=user)
      return Response({
        "status": status.HTTP_200_OK,
        "message": "you have successfully logged in ",
        "token": str(token)
      })


class LogoutView(APIView): 

  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
  
  def get(self, request):
    request.user.auth_token.delete()
    return Response({
      "status": status.HTTP_200_OK,
      "message": "You have successfully logged out"
    })
  


class BlogView(APIView):
  
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    all_blog=AllBlog.objects.all()
    serial_blog=BlogSerializer(all_blog, many=True,   )
    return Response({
      "status": status.HTTP_200_OK,
      "message": "successfully got the data",
      "body": serial_blog.data
    })

  def post(self, request):
    post_blog=BlogSerializer(data=request.data)
    if post_blog.is_valid(): 
      post_blog.save(owner=request.user)
      return Response({
        "status": status.HTTP_201_CREATED,
        "message": "Blog successfully posted! "
      })
    return Response({
      "status": status.HTTP_400_BAD_REQUEST,
      "message": post_blog.errors
    })

class MyblogsView(APIView):

  permission_classes=[IsAuthenticated]
  authentication_classes=[TokenAuthentication]
  
  def get(self, request):
    blogs=AllBlog.objects.filter(owner=request.user)
    serial_blog=BlogSerializer(blogs, many=True)
    return Response({
      "status": status.HTTP_200_OK,
      "message": "Successfully got the data",
      "body": serial_blog.data
    })


class BlogcredView(APIView):

  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]

  def put(self, request, pk):
    try:
      blog=AllBlog.objects.get(pk=pk)
    except:
      return Response({
        "status": status.HTTP_404_NOT_FOUND,
        "message": "Blog Doesn't exists",
        "body": ""
      })

    if blog.owner != request.user:
      return Response({
        "status": status.HTTP_204_NO_CONTENT,
        "message": "You can not change this blog "
      })

    serial_blog=BlogSerializer(blog, data=request.data)
    if serial_blog.is_valid():
      serial_blog.save()
      return Response({
        "status": status.HTTP_200_OK,
        "message": "Blog successfully Updated",
      })
    return Response({
      "status": status.HTTP_400_BAD_REQUEST,
      "message": "incomplete credentials "
    })

  
  def delete(self, request, pk):
    try:
      blog=AllBlog.objects.get(pk=pk)
    except:
      return Response({
        "status": status.HTTP_404_NOT_FOUND,
        "message": "Blog Doesn't exists",
        "body": ""
      })

    if blog.owner != request.user:
      return Response({
        "status": status.HTTP_204_NO_CONTENT,
        "message": "You can not delete this blog "
      })

    blog.delete()
    return Response({
      "status": status.HTTP_204_NO_CONTENT,
      "message": "Blog Successfully deleted"
    })
  