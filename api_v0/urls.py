from django.urls import path
from .views import NewsListAPIView,NewsDetailAPIView

urlpatterns = [
    path('', NewsListAPIView.as_view(), name="news-list"),
    path('news-detail/<str:pk>/', NewsDetailAPIView.as_view(), name="news-detail"),
]