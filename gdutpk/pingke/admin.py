from django.contrib import admin

from django.db import models
from django import forms
from .models import *

# Register your models here.

#class GdutGuestAdmin(admin.ModelAdmin):
#	list_display = ('id', 'username', 'email', 'date_joined', 'last_login', 'review_count')

admin.site.register(GdutGuest)
admin.site.register(GdutUser)
admin.site.register(Dept)
admin.site.register(Major)
admin.site.register(Teacher)
#admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Review)
