from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import Report, Bamboo


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'content', 'message', 'bamboo')


class ReportViewSet(viewsets.mixins.CreateModelMixin,
                    viewsets.mixins.RetrieveModelMixin,
                    viewsets.mixins.DestroyModelMixin,
                    viewsets.mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_queryset(self):
        queryset = self.queryset
        if 'bamboo_pk' in self.kwargs:
            bamboo_pk = self.kwargs['bamboo_pk']
            bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
            queryset = queryset.filter(bamboo=bamboo)
        return queryset
