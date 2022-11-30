from django.urls import path
from . import views

urlpatterns = [
    path("", views.Wishlists.as_view()),
    path("<int:pk>", views.WishlistDetail.as_view()),
    path("<int:wishlist_pk>/fabric/<int:pk>", views.WishlistToggle.as_view()),
]
