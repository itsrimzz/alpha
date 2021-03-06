from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context
from django.contrib.auth.models import User, Group

from ..models import Order, Article, UserProfile, Notes


def home(request):
    pending_orders = Order.objects.exclude(status__in=['In Review', 'Completed', 'Canceled'])
    in_review_orders = Order.objects.filter(status='In Review')
    context = Context({'pending_orders': pending_orders, 'in_review_orders': in_review_orders})
    return render(request, "Dashboard_admin.html", context)


def order_view(request, context):
    return render(request, "project_info_page_agent_view.html", context)


def create_order(request):
    if request.method == "POST":
        article = Article.objects.create(title=request.POST['project-title'],
                                         assignment_type=request.POST['assignment-type'],
                                         discipline=request.POST['discipline'],
                                         instructions=request.POST['instructions'], pages=request.POST['pages'])
        customer = User.objects.get(email=request.POST['user'])
        assignee = User.objects.get(username=request.POST['assignee'])
        order = Order.objects.create(article=article, customer=customer, assignee=assignee,
                                     deadline=request.POST['deadline'], currency=request.POST['currency'],
                                     estimated_budget=request.POST['budget'], status=request.POST['project-status'])
        return render(request, "blank.html", {"page_title": "Order created successfully"})
    else:
        customer_list = User.objects.filter(groups__name='customer')
        agents_list = User.objects.filter(groups__name__in=['agent', "admin"])
        return render(request, "project_info_page.html",
                      {"status_choices": Order.STATUS_CHOICES, "assignment_choices": Article.ASSIGNMENT_CHOICES,
                       "currency_choices": Order.CURRENCY_CHOICES, "customer_list": customer_list,
                       "agents_list": agents_list})


def create_user(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if len(user) != 0:
            return render(request, "blank.html", {"page_title": "User Already exists !"})
        user, created = User.objects.get_or_create(username=request.POST['email'], email=request.POST['email'],
                                                   first_name=request.POST['first-name'],
                                                   last_name=request.POST['last-name'], )
        if created:
            user.set_password(request.POST['password'])
            user.save()
            group = Group.objects.get(name=request.POST['group'])
            user.groups.add(group)
            UserProfile.objects.create(user=user, phone_number=request.POST['phone'], skype_name=request.POST['skype'])
            return render(request, "blank.html", {"page_title": "User created successfully !"})
            # user was created
            # set the password here
        else:
            return render(request, "blank.html", {"page_title": "User Already exists !"})
    else:
        return render(request, "new_user.html", {"group_list": Group.objects.all()})


def get_completed_orders(request):
    completed_orders = Order.objects.filter(status='Completed')
    return render(request, "completed_orders.html", {'completed_orders': completed_orders})


def get_cancelled_orders(request):
    cancelled_orders = Order.objects.filter(status='Canceled')
    return render(request, "cancelled_orders.html", {'cancelled_orders': cancelled_orders})
