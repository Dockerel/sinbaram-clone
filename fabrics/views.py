from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Fabric
from .serializer import FabricSerializer, FabricDetailSerializer
from reviews.serializer import ReviewSerializer
from qnas.serializer import QnaSerializer, NewQnaSerializer


class Fabrics(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        all_fabrics = Fabric.objects.all()
        serializer = FabricSerializer(
            all_fabrics,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = FabricSerializer(data=request.data)
        if serializer.is_valid():
            fabric = serializer.save()
            serializer = FabricSerializer(fabric)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class FabricDetail(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Fabric.objects.get(pk=pk)
        except Fabric.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        fabric = self.get_object(pk)
        serializer = FabricDetailSerializer(fabric)
        return Response(serializer.data)

    def put(self, request, pk):
        fabric = self.get_object(pk)
        serializer = FabricDetailSerializer(
            fabric,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_fabric = serializer.save()
            serializer = FabricDetailSerializer(updated_fabric)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_204_NO_CONTENT,
            )

    def delete(self, request, pk):
        fabric = self.get_object(pk)
        fabric.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class FabricReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Fabric.objects.get(pk=pk)
        except Fabric.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        fabric = self.get_object(pk)
        review = fabric.reviews.all()
        serializer = ReviewSerializer(
            review,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(user=request.user, fabric=self.get_object(pk))
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FabricQuestions(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Fabric.objects.get(pk=pk)
        except Fabric.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        fabric = self.get_object(pk)
        qna = fabric.qnas.all()
        serializer = QnaSerializer(
            qna,
            many=True,
        )
        return Response(serializer.data)


class NewFabricQuestions(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = NewQnaSerializer(data=request.data)
        if serializer.is_valid():
            new_qna = serializer.save(user=request.user)
            serializer = NewQnaSerializer(new_qna)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
