from django.urls import path
from . import views

urlpatterns = [
    path("", views.Fabrics.as_view()),
    path("<int:pk>", views.FabricDetail.as_view()),
    path("<int:pk>/reviews", views.FabricReviews.as_view()),
    path("<int:pk>/questions", views.FabricQuestions.as_view()),
    path("<int:pk>/questions/new", views.NewFabricQuestions.as_view()),
    path("<int:fabric_pk>/questions/<int:pk>", views.FabricQuestionsDetail.as_view()),
    path("<int:fabric_pk>/questions/<int:pk>/answer", views.FabricQuestionsAnswer.as_view()),
]
