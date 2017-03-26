from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article (models.Model):
    ASSIGNMENT_CHOICES = (
        ('Essay', 'Essay'),
        ('Others', 'Others'),
    )
    title = models.CharField(max_length=100)
    assignment_type = models.CharField(max_length=50, choices=ASSIGNMENT_CHOICES, null=True, blank=True)
    discipline = models.CharField(max_length=50, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)


class Order (models.Model):
    STATUS_CHOICES = (
        ('initiated', 'Initiated'),
        ('In Progress', 'In Progress'),
        ('In Review', 'In Review'),
        ('Completed', 'Completed'),
        ('Canceled','Canceled'),
    )
    customer = models.ForeignKey(User, related_name="customer")
    made_on  = models.DateTimeField(default = datetime.now)
    deadline = models.DateTimeField()
    estimated_budget = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    article = models.ForeignKey(Article)
    assignee = models.ForeignKey(User, related_name="assignee", null=True, blank=True)

class UserProfile (models.Model):
    user = models.ForeignKey(User)
    skype_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class Notes (models.Model):
    order = models.ForeignKey(Order)
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User)
    made_on = models.DateTimeField(default= datetime.now)