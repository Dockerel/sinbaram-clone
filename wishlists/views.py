from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Wishlist
from .serializer import WishlistSerializer


class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(
            all_wishlists,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            new_wishlist = serializer.save(
                user=request.user,
            )
            serializer = WishlistSerializer(new_wishlist)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class WishlistDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)

    def put(self, request, pk):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(
            wishlist,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_wishlist = serializer.save()
            serializer = WishlistSerializer(updated_wishlist)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        wishlist = self.get_object(pk)
        wishlist.delete()
        return Response(status=status.HTTP_200_OK)
