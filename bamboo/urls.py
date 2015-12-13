from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api.views.bamboo import BambooViewSet
from api.views.comment import CommentViewSet
from api.views.manager import BambooManagerViewSet
from api.views.post import PostViewSet
from api.views.report import ReportViewSet
from api.views.user import UserViewSet

router = routers.DefaultRouter()

# Register API URLs\
router.register(r'user', UserViewSet)
router.register(r'bamboo', BambooViewSet)
router.register(r'bamboo/(?P<bamboo_pk>.+)/manager', BambooManagerViewSet,
                base_name='manager')


urlpatterns = patterns(
    '',
    # Post CRUD URLs
    url(r'^bamboo/(?P<bamboo_pk>.+)/post/$', PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^bamboo/(?P<bamboo_pk>.+)/post/(?P<post_number>.+)/$',
        PostViewSet.as_view({
            'get': 'retrieve',
            'delete': 'destroy',
        })),
    # Report CRUD URLs
    url(r'^bamboo/(?P<bamboo_pk>.+)/report/$', ReportViewSet.as_view({
        'post': 'create',
        'get': 'list',
    })),
    url(r'^report/(?P<pk>.+)/$', ReportViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
    })),
    # Comment CRUD URLs
    url(r'^post/(?P<post_pk>.+)/comment/$', CommentViewSet.as_view({
        'post': 'create',
        'get': 'list',
    })),
    url(r'^comment/(?P<pk>.+)/$', CommentViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
    })),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
