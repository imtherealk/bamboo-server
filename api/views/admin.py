from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import BambooAdmin


class BambooAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BambooAdmin
        fields = ('id', 'admin', 'bamboo', 'created_at')


class BambooAdminViewSet(viewsets.ModelViewSet):
    queryset = BambooAdmin.objects.all()
    serializer_class = BambooAdminSerializer
