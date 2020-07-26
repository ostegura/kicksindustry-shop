import django_filters

from .models import Shoes, ShoesSize, Category
from django.forms.widgets import TextInput

# def shoes_queryset(request):
#     return ShoesSize.objects.all()


class ShoesFilter(django_filters.FilterSet):

    CHOICES = (
        ('popularity', 'Популярности'),
        ('price_up', 'Цена возр.'),
        ('price_down', 'Цена уб.'),
    )
    price__gt = django_filters.NumberFilter(label='Цена от:', field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(label='Цена до:', field_name='price', lookup_expr='lte')
    model = django_filters.CharFilter(label='', field_name='model', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Поиск..'}))

    # shoes = django_filters.ModelChoiceFilter(queryset=shoes_queryset, label='')

    ordering = django_filters.ChoiceFilter(label='Сортировать по:', choices=CHOICES, method='filter_by_price')

    class Meta:
        model = Shoes
        fields = {
            'model': ['icontains'],
        }

    def filter_by_price(self, queryset, name, value):
        expression = ''

        if value == 'price_up':
            expression = 'price'
        elif value == 'price_down':
            expression = '-price'
        elif value == 'popularity':
            expression = '-sale_cnt'
        return queryset.order_by(expression)



# # TODO add shoes size filter
# class ShoesSizeFilter(django_filters.FilterSet):
#
#     size = django_filters.NumberFilter(label='Размер:', field_name='model_size', lookup_expr='icontains')
#
#     class Meta:
#         model = ShoesSize
#         fields = {
#             'model_size': ['icontains']
#         }