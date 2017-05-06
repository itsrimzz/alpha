from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

from .models import Order, Article, UserProfile, Notes

from .roles import agent, admin_role, cem, customer

# Create your views here.


@login_required
def home(request):
    if request.user.groups.filter(name=settings.AGENT).exists():
        return agent.home(request)
    elif request.user.groups.filter(name=settings.ADMIN).exists():
        return admin_role.home(request)
    elif request.user.groups.filter(name=settings.CEM).exists():
        return cem.home(request)
    elif request.user.groups.filter(name=settings.CUSTOMER).exists():
        return customer.home(request)
    else:
        return HttpResponse("This User doesnot belong to any registered group. Please add this user to some group")


@login_required
def order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    notes = Notes.objects.filter(order = order)
    context = {"order": order, "notes": notes}
    if request.user.groups.filter(name=settings.AGENT).exists():
        return agent.order_view(request, context)
    elif request.user.groups.filter(name=settings.ADMIN).exists():
        return admin_role.order_view(request, context)
    elif request.user.groups.filter(name=settings.CEM).exists():
        return cem.order_view(request, context)
    elif request.user.groupd.filter(name=settings.CUSTOMER).exists():
        return customer.order_view(request, customer)
    else:
        return HttpResponse("This User doesnot belong to any registered group. Please add this user to some group")


@login_required
def create_order(request):
    if request.user.groups.filter(name=settings.ADMIN).exists():
        return admin_role.create_order(request)
    elif request.user.groups.filter(name=settings.CEM).exists():
        return cem.create_order(request)
    else:
        return redirect(home)


@login_required
def create_user(request):
    if request.user.groups.filter(name=settings.ADMIN).exists():
        return admin_role.create_user(request)
    elif request.user.groups.filter(name=settings.CEM).exists():
        return cem.create_user(request)
    else:
        return redirect(home)


@login_required
def completed_orders(request):
    if request.user.groups.filter(name=settings.ADMIN).exists():
        return admin_role.get_completed_orders(request)
    elif request.user.groups.filter(name=settings.CEM).exists():
        return cem.get_completed_orders(request)
    else:
        return redirect(home)


@login_required
def cancelled_orders(request):
    if request.user.groups.filter(name=settings.ADMIN).exists():
        return admin_role.get_cancelled_orders(request)
    elif request.user.groups.filter(name=settings.CEM).exists():
        return cem.get_cancelled_orders(request)
    else:
        return redirect(home)


@login_required
def create_note(request):
    order = Order.objects.get(id = request.POST["order-id"])
    Notes.objects.create(user = request.user, text = request.POST['text'], order = order)
    return redirect('/order/'+str(order.id))
