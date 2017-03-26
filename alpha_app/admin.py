from django.contrib import admin
from .models import Article, Order, UserProfile, Notes

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title','pages']



class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'deadline']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'skype_name']

class NoteAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'made_on']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Notes, NoteAdmin)