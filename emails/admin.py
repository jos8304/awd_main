from django.contrib import admin
from .models import List, Report, Email, EmailTracking
# Register your models here.

admin.site.register(List)
admin.site.register(Report)
admin.site.register(Email)
admin.site.register(EmailTracking)