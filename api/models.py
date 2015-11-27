from django.db import models
from django.contrib.auth.models import AbstractUser


class CreatedAtMixin(object):
    created_at = models.DateTimeField(auto_now_add=True)


class Model(models.Model):
    def __str__(self):
        return str(self.id)

    class Meta(object):
        abstract = True


class User(AbstractUser):
    pass


class Bamboo(Model, CreatedAtMixin):
    name = models.CharField(max_length=20)
    notice = models.TextField(null=True, blank=True)
    admins = models.ManyToManyField(User, through='BambooAdmin')


class Report(Model, CreatedAtMixin):
    content = models.TextField()
    message = models.TextField(null=True, blank=True)
    bamboo = models.ForeignKey(Bamboo)
    writer = models.ForeignKey(User)


class Post(Model, CreatedAtMixin):
    post_number = models.IntegerField()
    admin = models.ForeignKey(User)
    report = models.ForeignKey(Report)


class Comment(Model, CreatedAtMixin):
    content = models.TextField()
    writer = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class BambooAdmin(Model, CreatedAtMixin):
    admin = models.ForeignKey(User)
    bamboo = models.ForeignKey(Bamboo)
