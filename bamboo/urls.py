from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api.views.bamboo import BambooViewSet
from api.views.comment import CommentViewSet
from api.views.post import PostViewSet
from api.views.report import ReportViewSet
from api.views.user import UserViewSet

router = routers.DefaultRouter()

# Register API URLs
router.register(r'user', UserViewSet)
router.register(r'bamboo', BambooViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'post', PostViewSet)
router.register(r'report', ReportViewSet)



urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
