from django.contrib import admin
from api import models

admin.site.register(models.Bamboo)
admin.site.register(models.Comment)
admin.site.register(models.Post)
admin.site.register(models.Report)
admin.site.register(models.User)
admin.site.register(models.BambooManager)
