from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context
from django.contrib.auth.models import User, Group

from ..models import Order, Article, UserProfile, Notes


def home(request):
    pending_orders = Order.objects.exclude(status__in=['In Review', 'Completed', 'Canceled'])
    pending_orders = pending_orders.filter(assignee=request.user)
    in_review_orders = Order.objects.filter(status='In Review')
    in_review_orders = in_review_orders.filter(assignee=request.user)
    context = Context({'pending_orders': pending_orders, 'in_review_orders': in_review_orders})
    return render(request, "Dashboard_agent.html", context)


def order_view(request, context):
    return render(request, "project_info_page_agent_view.html", context)
