from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    #user = models.ForeignKey(User, on_delete= models.CASCADE, null = TRue, blank=True)
    title = models.CharField(max_lenght=200)
    detail = models.TextField(null=True, blank = True)
    complete = models.BooleanFiled(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
