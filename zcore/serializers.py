from cloudinary.forms import CloudinaryJsFileField
from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image = CloudinaryJsFileField(required=True)
    caption = serializers.CharField(max_length=100)

    class Meta:
        model = Image
        fields = ['id', 'image', 'caption']
