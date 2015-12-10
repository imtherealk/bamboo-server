from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets

from api.models import Post, Bamboo, Report


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_number', 'content',
                  'bamboo', 'writer', 'created_at', 'confirmed_by')


class PostViewSet(viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.queryset
        if 'bamboo_pk' in self.kwargs:
            bamboo_pk = self.kwargs['bamboo_pk']
            bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
            queryset = queryset.filter(bamboo=bamboo)
        return queryset

