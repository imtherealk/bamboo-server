from django.contrib import admin
from api.models import Bamboo, Comment, Post, Report, User, BambooAdmin

admin.site.register(Bamboo)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Report)
admin.site.register(User)
admin.site.register(BambooAdmin)
