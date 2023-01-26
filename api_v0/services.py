from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination 
from news.models import News



class NewsFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title',lookup_expr='icontains')

    class Meta:
        model = News
        fields = ['title']

       
class NewsAPIPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20