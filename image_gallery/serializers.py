from rest_framework import serializers
from .models import ImageGallery, Image, UserProfile

class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = '__all__'

    def create(self, validated_data):
        try:
            return ImageGallery.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(str(e))

class ImageSerializer(serializers.ModelSerializer):
    gallery_name = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'description', 'gallery', 'gallery_name']

    def get_gallery_name(self, obj):
        return obj.gallery.name
    def create(self, validated_data):
        try:
            return Image.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(str(e))

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        try:
            return UserProfile.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(str(e))
