from django.forms import forms
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models import Comment, Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'post')


class CommentCreateForm(forms.Form):
    content = forms.Field()


class CommentViewSet(viewsets.mixins.RetrieveModelMixin,
                     viewsets.mixins.DestroyModelMixin,
                     viewsets.mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = self.queryset
        if 'post_pk' in self.kwargs:
            post_pk = self.kwargs['post_pk']
            post = get_object_or_404(Post.objects.filter(id=post_pk))
            queryset = queryset.filter(post=post)
        return queryset

    def create(self, request, post_pk):
        post = get_object_or_404(Post.objects.filter(id=post_pk))
        form = CommentCreateForm(request.data)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment.objects.create(
                content=content,
                post=post,
                writer=request.user,
            )
            comment.save()
            serializer = self.get_serializer(comment)
            return Response(serializer.data, 201)
        return Response(form.errors, 400)
