from django.contrib import admin

# Register your models here.
from .models import JobModel

admin.site.register(JobModel)