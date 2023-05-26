from django.shortcuts import render
from .forms import OrderSearchForm
from cart.models import Order
from django.db.models import Q


def history_list(request):
    form = OrderSearchForm(request.POST or None)
    orders = []

    if form.is_valid():
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']

        if email or phone:
            # orders = Order.objects.filter(email=email, phone=phone)
            orders = Order.objects.filter(Q(email=email) | Q(phone=phone))

    context = {
        'form': form,
        'orders': orders
    }

    return render(request, 'history/order_list.html', context)
