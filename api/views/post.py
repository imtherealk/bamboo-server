from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_number', 'created_at', 'admin')


class PostViewSet(viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
