from django.contrib import admin
from .models import Contact,Student,Employee,Task,Profile

# Register your models here.

admin.site.register(Contact)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Student)
admin.site.register(Profile)



