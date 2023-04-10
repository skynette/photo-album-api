from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    caption = serializers.CharField(max_length=100)

    class Meta:
        model = Image
        fields = ['id', 'image', 'caption']
