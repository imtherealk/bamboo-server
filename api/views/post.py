from django.db import transaction
from django.forms import forms, fields
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from api.models import Post, Bamboo, Report
from api.views.user import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    writer = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'post_number', 'content',
                  'bamboo', 'writer', 'created_at', 'confirmed_by')


class PostCreateForm(forms.Form):
    report = fields.IntegerField()

    def clean_report(self):
        report = self.cleaned_data['report']
        report = Report.objects.filter(id=report).first()
        if report is None:
            raise forms.ValidationError("No such report.")
        return report


class PostViewSet(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.queryset
        if 'bamboo_pk' in self.kwargs:
            bamboo_pk = self.kwargs['bamboo_pk']
            bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
            queryset = queryset.filter(bamboo=bamboo)
        return queryset

    @transaction.atomic
    def create(self, request, bamboo_pk):
        bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
        form = PostCreateForm(request.data)
        if form.is_valid():
            report = form.cleaned_data['report']
            post = Post.objects.create(
                post_number=bamboo.next_post_number,
                content=report.content,
                bamboo=bamboo,
                writer=report.writer,
                confirmed_by=request.user,
            )
            bamboo.next_post_number += 1
            post.save()
            bamboo.save()
            serializer = self.get_serializer(post)
            return Response(serializer.data, 201)
        return Response(form.errors, 400)

    def retrieve(self, request, bamboo_pk, post_number):
        queryset = self.get_queryset()
        queryset = queryset.filter(post_number=post_number)
        post = queryset.first()
        if post is None:
            raise Http404()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def destroy(self, request, bamboo_pk, post_number):
        queryset = self.get_queryset()
        queryset = queryset.filter(post_number=post_number)
        post = queryset.first()
        if post is None:
            raise Http404()
        post.delete()
        return Response(None, 204)
