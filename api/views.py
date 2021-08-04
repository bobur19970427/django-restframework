from django.shortcuts import render
from .serializers import CategoryListAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Category
from rest_framework.views import APIView #kelayotgan so'rovni get yoki postligini aniqlab beradi

from rest_framework.response import Response #json ko'rinishida javob qaytaradi

from rest_framework.parsers import JSONParser #jsoni ob'yektga o'tkazib beradi va request.data ni ichiga joylashtiradi

from django.contrib.auth.models import User #djangoni o'zini tayyor foydalanuvchi modelini chaqirib olamiz

from rest_framework.authtoken.models import Token #rest_frameworkning token modelini chaqirib olamiz

from django.contrib.auth import authenticate #va djangoni foydalanuvchi login parolini tekshiradigan funksiya
# Create your views here.

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListAPIView

class CreateCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListAPIView

class CategoryUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListAPIView

class CategoryDelete(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListAPIView

class SignUp(APIView):
    def post(self,request):
        parser_classes = JSONParser
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        user_check = User.objects.filter(username=username).exists()
        if user_check:
            return Response({"code":"Bunday foydalanuvchioldin ro'yxatdan o'tgan"})
        else:
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            token,create = Token.objects.get_or_create(user=user)
            return Response({"token":str(token)})
class SignIn(APIView):
    def post(self,request):
        parser_classes = JSONParser #kelayotgan jsoni obyektga o'tkazib beradi
        username = request.data['username']
        password = request.data['password']
        if username is None or password is None:
            return Response({"code":"username yoki passwordni to'ldirmagansiz"})
        user = authenticate(username=username,password=password)
        if not user:
            return Response({"code":"login yoki parol noto'g'ri qayta urinib ko'ring"})
        token,create = Token.objects.get_or_create(user=user)
        return Response({"token":str(token)})
