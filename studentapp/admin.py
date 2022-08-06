from django.contrib import admin

# Register your models here.
from studentapp import models

admin.site.register(models.Login)
admin.site.register(models.School)
admin.site.register(models.Course)
admin.site.register(models.Student)