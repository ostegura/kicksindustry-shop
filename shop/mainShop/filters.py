import django_filters
from .models import Shoes


class ShoesFilter(django_filters.FilterSet):

    CHOICES = (
        ('price_up', 'Цена возр.'),
        ('price_down', 'Цена уб.')
    )
    price_gt = django_filters.NumberFilter(label='Цена от:', field_name='price', lookup_expr='gte')
    price_lt = django_filters.NumberFilter(label='Цена до:', field_name='price', lookup_expr='lte')

    ordering = django_filters.ChoiceFilter(label='Сортировать по:', choices=CHOICES, method='filter_by_price')

    class Meta:
        model = Shoes
        fields = {
            # 'price': ['gte', 'lte'],
            'model': ['icontains'],
        }

    def filter_by_price(self, queryset, name, value):
        expression = 'price' if value == 'price_up' else '-price'
        return queryset.order_by(expression)



# TODO add shoes size filter
class ShoesSizeFilter():
    pass