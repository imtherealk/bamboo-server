from rest_framework import serializers, viewsets

from api.models import BambooManager


class BambooAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BambooManager
        fields = ('id', 'manager', 'created_at')


class BambooAdminViewSet(viewsets.ModelViewSet):
    queryset = BambooManager.objects.all()
    serializer_class = BambooAdminSerializer

    def get_queryset(self):
        bamboo_pk = self.kwargs['bamboo_pk']
        queryset = self.queryset.filter(bamboo__id=bamboo_pk)
        return queryset
