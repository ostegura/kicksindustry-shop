import django_filters

from .models import Shoes, ShoesSize, Category, ModelSizeList
from django.forms.widgets import TextInput


# def get_shoesSize_qs(request):
#     if request is None:
#         return ShoesSize.objects.none()
#
#     shoes = request.shoes.modelsizelist
#     return shoes.shoessize_set.all()


class ShoesFilter(django_filters.FilterSet):

    CHOICES = (
        ('popularity', 'Популярности'),
        ('price_up', 'Цена возр.'),
        ('price_down', 'Цена уб.'),
    )
    price__gt = django_filters.NumberFilter(label='Цена от:', field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(label='Цена до:', field_name='price', lookup_expr='lte')
    model = django_filters.CharFilter(label='', field_name='model', lookup_expr='icontains',
                                      widget=TextInput(attrs={'placeholder': 'Поиск..'}))

    # test = django_filters.RangeFilter(field_name='price', lookup_expr='', label='Цена от и до:')

    # size = django_filters.ModelMultipleChoiceFilter(queryset=get_shoesSize_qs, label='Размер:', field_name='modelsizelist__shoessize__model_size')
    size = django_filters.CharFilter(label='Размер: ', field_name='modelsizelist__shoessize__model_size',
                                     lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Введите размер..'}))

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

    # def filter_by_size(self, queryset, name, value):
    #     pass