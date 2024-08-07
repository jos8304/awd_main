from django.contrib import admin
from .models import Student,Tickets, Employee
# Register your models here.

admin.site.register(Student)
admin.site.register(Tickets)
admin.site.register(Employee)