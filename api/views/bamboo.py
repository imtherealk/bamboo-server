from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import Bamboo


class BambooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bamboo
        fields = ('id', 'name', 'created_at', 'notice')


class BambooViewSet(viewsets.ModelViewSet):
    queryset = Bamboo.objects.all()
    serializer_class = BambooSerializer
