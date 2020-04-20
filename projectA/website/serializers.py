from rest_framework import serializers
from .models import Category, Movie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'id')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'image')


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'image', 'description', 'directors',
                  'actors', 'scenarist', 'producer', 'genres', 'release_date',
                  'total_duration', 'country', 'budget', 'category', 'id')
