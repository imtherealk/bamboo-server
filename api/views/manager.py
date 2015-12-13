from django.forms import forms, fields
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from api.models import BambooManager, Bamboo, User
from api.views.user import UserSerializer


class ManagerCreateForm(forms.Form):
    user = fields.IntegerField()

    def clean_user(self):
        user = self.cleaned_data['user']
        user = User.objects.filter(id=user).first()
        if user is None:
            raise forms.ValidationError("No such user.")
        return user


class BambooManagerViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        bamboo_pk = self.kwargs['bamboo_pk']
        bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
        queryset = bamboo.managers.all()
        return queryset

    def list(self, request, bamboo_pk):
        queryset = self.get_queryset()
        managers = queryset.all()
        serializer = self.get_serializer(managers, many=True)
        return Response(serializer.data)

    def create(self, request, bamboo_pk):
        bamboo = get_object_or_404(Bamboo.objects.filter(id=bamboo_pk))
        form = ManagerCreateForm(request.data)
        if form.is_valid():
            user = form.cleaned_data['user']
            if BambooManager.objects.filter(
                    manager=user,
                    bamboo=bamboo).exists():
                form.add_error('user', "Already manager.")
                return Response(form.errors, 400)
            BambooManager.objects.create(
                manager=user,
                bamboo=bamboo,
            ).save()
            serializer = self.get_serializer(user)
            return Response(serializer.data, 201)
        return Response(form.errors, 400)

    def destroy(self, request, bamboo_pk, pk):
        bamboo_manager = get_object_or_404(BambooManager.objects.filter(
            manager=pk,
            bamboo=bamboo_pk))
        bamboo_manager.delete()
        return Response(None, 204)
