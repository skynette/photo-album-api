from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ListField(child=serializers.ImageField(), required=True)

    class Meta:
        model = Image
        fields = ['id', 'image', 'caption']
