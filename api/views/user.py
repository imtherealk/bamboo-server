from rest_framework import serializers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny, BasePermission

from api.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        if request.user.is_superuser:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj == request.user:
            return True
        return False


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
