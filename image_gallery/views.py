from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Image
from .permissions import HasFullAccess, HasViewAccess
from .serializers import ImageSerializer

class ImageGalleryAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasFullAccess]

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasFullAccess]

    def get(self,request, pk):
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Image.DoesNotExist:
            return Response({'message': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Image updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Image.DoesNotExist:
            return Response({'message': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request, pk):
        try:
            image = Image.objects.get(pk=pk)
            image.delete()
            return Response({'message': 'Image deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Image.DoesNotExist:
            return Response({'message': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

class ViewImageGalleryAPIView(APIView):
    permission_classes = [IsAuthenticated, HasViewAccess]

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        raise PermissionDenied(detail="You do not have permission to perform this action.")

    def put(self,request, pk):
        return Response({'message': 'No permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self,request, pk):
        return Response({'message': 'No permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)
