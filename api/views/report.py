from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route

from api.models import Report


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'content', 'message', 'created_at', 'bamboo')


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
