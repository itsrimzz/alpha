from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context
from django.contrib.auth.models import User, Group

from ..models import Order, Article, UserProfile, Notes


def home(request):
    return HttpResponse("Hello Customer")


def order_view(request, context):
    return HttpResponse("No view has been defined yet")