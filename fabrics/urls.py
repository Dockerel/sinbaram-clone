from django.urls import path
from . import views

urlpatterns = [
    path("", views.Fabrics.as_view()),
    path("<int:pk>", views.FabricDetail.as_view()),
]
