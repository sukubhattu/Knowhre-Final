from . models import Company
import django_filters

class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Company
        fields = ['name', 'category']