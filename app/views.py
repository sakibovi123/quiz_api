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

    def get(self, request):
        query = QuizType.objects.all()
        serializer = QuizTypeSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuizTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizTypeEditView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, type_id):
        quiz_obj = get_object_or_404(QuizType, id=type_id)
        quiz_obj.type_name = request.data["type_name"]
        quiz_obj.save()
        serializer = QuizTypeSerializer(quiz_obj)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class QuizTypeDelete(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, type_id):
        quiz_obj = get_object_or_404(QuizType, id=type_id)
        quiz_obj.delete()
        serializer = QuizTypeSerializer(quiz_obj)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class QuizGet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = Quiz.objects.all()
        serializer = QuizSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizPost(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = request.user
        quiz = Quiz(
            user=user,
            category=Category.objects.get(id=request.data["category"]),
            quiz_title=request.data["quiz_title"],
        )

        quiz.save()

        for o in request.data["options"]:
            answer = Answer.objects.create(title=o["title"])
            quiz.options.add(answer)

        for c in request.data["correct_answer"]:
            obj = Answer.objects.get(title=c["title"])
            quiz.correct_answer.add(obj)

        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
