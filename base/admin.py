from django.contrib import admin
from .models import Course, Category, Event, Message, Chat
# Register your models here.

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Message)
admin.site.register(Chat)