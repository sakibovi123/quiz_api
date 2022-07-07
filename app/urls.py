from django.urls import path, include
from app.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='LoginView'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", UserRegisterView.as_view()),

    # Quiz Type Paths
    path("quiz-types/", QuizTypePostView.as_view()),
    path("edit-type/<int:type_id>/", QuizTypeEditView.as_view()),
    path("delete-type/<int:type_id>/", QuizTypeDelete.as_view()),

    # Category paths
    # path("category/", QuizTypePostView.as_view()),
    # path("category/<int:category_id>/", QuizTypeEditView.as_view()),
    # path("category/<int:category_id>/", QuizTypeDelete.as_view()),

    # Answer paths

    # Quiz paths
    path("quizs/", QuizGet.as_view()),
    path("create-quiz/", QuizPost.as_view()),

    # Submit
    path("submits/", GetSubmission.as_view()),
]