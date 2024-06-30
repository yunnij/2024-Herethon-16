from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Portfolio, Career,Video, Photo

class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'role', 'profile_photo', 'email', 'one_line', 'intro']

class CareerSerializer(ModelSerializer):
    career_year = serializers.DateField(format="%Y") # 연도만
    class Meta:
        model = Career
        fields = ['id', 'career_title', 'career_role', 'career_year', 'portfolio']

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'likes_user', 'cast', 'staff', 'price', 'keyword', 'synopsis', 'video', 'portfolio']

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo', 'portfolio']