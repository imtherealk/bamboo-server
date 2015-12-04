from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import BambooManager


class BambooAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BambooManager
        fields = ('id', 'admin', 'bamboo', 'created_at')


class BambooAdminViewSet(viewsets.ModelViewSet):
    queryset = BambooManager.objects.all()
    serializer_class = BambooAdminSerializer
