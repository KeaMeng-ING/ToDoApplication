from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'complete', 'created')  # Fields to display


    