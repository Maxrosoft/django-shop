from django.shortcuts import render, get_object_or_404
from .models import Shop, Product
from cart.forms import CartAddProductForm


class ShopViews:
    def __init__(self) -> None:
        self.first = True
        self.slug = ''

    def product_list(self, request, shop_slug=None):
        shop = None
        shops = Shop.objects.all()
        products = Product.objects.all()
        cart_product_form = CartAddProductForm()
        if shop_slug:
            if self.first:
                shop = get_object_or_404(Shop, slug=shop_slug)
                products = products.filter(shop=shop)
                self.first = False
                self.slug = shop_slug
        if self.slug:
            shop = get_object_or_404(Shop, slug=self.slug)
            products = products.filter(shop=shop)
        return render(request, 'myshop/shop/list.html',
            {'shop': shop,
            'shops': shops,
            'products': products,
            'cart_product_form': cart_product_form,
            'first': self.first})