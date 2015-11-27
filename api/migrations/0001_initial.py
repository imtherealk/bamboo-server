# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
from django.conf import settings
import api.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username', unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(to='auth.Group', related_query_name='user', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bamboo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('notice', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.CreatedAtMixin),
        ),
        migrations.CreateModel(
            name='BambooAdmin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('bamboo', models.ForeignKey(to='api.Bamboo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.CreatedAtMixin),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.CreatedAtMixin),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('post_number', models.IntegerField()),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.CreatedAtMixin),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', models.TextField()),
                ('message', models.TextField(null=True, blank=True)),
                ('bamboo', models.ForeignKey(to='api.Bamboo')),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.CreatedAtMixin),
        ),
        migrations.AddField(
            model_name='post',
            name='report',
            field=models.ForeignKey(to='api.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='api.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bamboo',
            name='admins',
            field=models.ManyToManyField(through='api.BambooAdmin', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
