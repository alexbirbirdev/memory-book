from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models import News
from ..serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(is_published=True).order_by('-publish_date')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'publish_date', 'is_published']
    search_fields = ['title', 'short_description', 'content']
    ordering_fields = ['publish_date']