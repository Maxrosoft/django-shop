from django.urls import path
from . import views

app_name = 'shop'

product_list = views.ShopViews().product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:shop_slug>/', product_list,
        name='product_list_by_shop'),
]