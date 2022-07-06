from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            response_data= {
                "refresh": str(token),
                "access": str(token.access_token),
                "user": serializer.data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


