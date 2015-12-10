from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import Comment, Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'post')


class CommentViewSet(viewsets.mixins.CreateModelMixin,
                     viewsets.mixins.RetrieveModelMixin,
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

