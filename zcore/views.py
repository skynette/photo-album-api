from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import cloudinary.uploader
from .models import Image
from .serializers import ImageSerializer

class ImageListCreateView(APIView):
    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_data = serializer.validated_data['image']
            upload_result = cloudinary.uploader.upload(image_data)
            serializer.save(image=upload_result['public_id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
