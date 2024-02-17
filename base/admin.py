from django.contrib import admin
from .models import Tasks, TasksAdmin
# Register your models here.
admin.site.register(Tasks, TasksAdmin)