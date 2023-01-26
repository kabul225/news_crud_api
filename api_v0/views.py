from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from news.models import News
from .serializer import NewsSerilizer
from .services import NewsFilter,NewsAPIPagination

class NewsListAPIView(ListCreateAPIView):
    serializer_class = NewsSerilizer
    queryset = News.objects.all().order_by('created')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter
    pagination_class = NewsAPIPagination
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class NewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerilizer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = News.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

