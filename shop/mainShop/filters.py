import django_filters
from .models import Shoes


class ShoesFilter(django_filters.FilterSet):

    class Meta:
        model = Shoes
        fields = {
            'price': ['gte', 'lte'],
            # 'model': ['icontains'],
        }
