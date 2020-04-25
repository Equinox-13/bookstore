from django.shortcuts import render
from django.views.generic.base import TemplateView


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
