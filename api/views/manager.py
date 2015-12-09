from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets

from api.models import BambooManager, Bamboo


class BambooAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BambooManager
        fields = ('id', 'manager', 'created_at')


class BambooAdminViewSet(viewsets.ModelViewSet):
    queryset = BambooManager.objects.all()
    serializer_class = BambooAdminSerializer

    def get_queryset(self):
        bamboo_pk = self.kwargs['bamboo_pk']
        bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
        queryset = self.queryset.filter(bamboo=bamboo)
        return queryset
