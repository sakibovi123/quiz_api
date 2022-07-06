from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(APIView):
    def post(self, request):
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


class QuizTypePostView(APIView):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def get(request):
        query = QuizType.objects.all()
        serializer = QuizTypeSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = QuizTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizTypeEditView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def put(request, type_id):
        quiz_obj = get_object_or_404(QuizType, id=type_id)
        quiz_obj.type_name = request.data["type_name"]
        quiz_obj.save()
        serializer = QuizTypeSerializer(quiz_obj)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class QuizTypeDelete(APIView):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def delete(request, type_id):
        quiz_obj = get_object_or_404(QuizType, id=type_id)
        quiz_obj.delete()
        serializer = QuizTypeSerializer(quiz_obj)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


