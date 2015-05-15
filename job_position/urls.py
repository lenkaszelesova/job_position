from django.conf.urls import include, url
from django.contrib import admin
from jobs import views
from rest_framework import routers

router  = routers.DefaultRouter()
router.register(r'job_position', views.Job_PositionViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('jobs.urls')),
    url(r'^admin/', include(admin.site.urls))
]
