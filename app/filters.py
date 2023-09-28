import django_filters
from django_filters import CharFilter
from .models import Hadith

class HadithFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='exact')
    detail = CharFilter(field_name='detail', lookup_expr='icontains')

    class Meta:
        model = Hadith
        fields = ['category',]