from django import forms
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from api.models import Report, Bamboo


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'content', 'message', 'bamboo', 'created_at')


class ReportCreateForm(forms.Form):
    content = forms.Field()
    message = forms.Field(required=False)


class ReportViewSet(viewsets.mixins.RetrieveModelMixin,
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

    def create(self, request, bamboo_pk):
        bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
        form = ReportCreateForm(request.data)
        if form.is_valid():
            content = form.cleaned_data['content']
            message = form.cleaned_data['message']
            report = Report.objects.create(
                content=content,
                message=message,
                bamboo=bamboo,
                writer=request.user,
            )
            report.save()
            serializer = self.get_serializer(report)
            return Response(serializer.data, 201)
        return Response(form.errors, 400)
