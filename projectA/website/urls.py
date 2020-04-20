from django.urls import path, include
from website.views import MovieView, CategoryView, MovieDetailView

urlpatterns = [
    path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('movie/list/', MovieView.as_view({'get': 'list', 'post': 'create'})),
    path('movie/<int:pk>/', MovieDetailView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]