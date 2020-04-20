from rest_framework import filters, status
from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework
from rest_framework.response import Response
from .models import Movie, Category
from .serializers import CategorySerializer, MovieSerializer, MovieDetailSerializer


class MovieView(ModelViewSet):
    filter_backends = ([django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter])
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_fields = ('title',)
    search_fields = ('title',)
    lookup_field = 'pk'


class MovieDetailView(ModelViewSet):
    filter_backends = ([django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter])
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
    filter_fields = ('title',)
    search_fields = ('title',)
    lookup_field = 'pk'


class CategoryView(ModelViewSet):
    filter_backends = ([django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter])
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_fields = ('title',)
    search_fields = ('title',)
    lookup_field = 'pk'
