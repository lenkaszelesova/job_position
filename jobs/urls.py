from django.conf.urls import url
from . import views
from .views import Job_PositionViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

job_position_list = Job_PositionViewSet.as_view({
	'get': 'list',
	'post': 'create'
	})

job_position_detail = Job_PositionViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
	})

user_list = UserViewSet.as_view({
	'get': 'list',
	})

user_detail = UserViewSet.as_view({
	'get': 'retrieve',
	})

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^job_position/$', job_position_list, name = 'job_position-list'),
    url(r'^job_position/(?P<pk>[0-9]+)/$', job_position_detail, name = 'job_position-detail'),
    url(r'^users/$', user_list, name = 'user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name = 'user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)