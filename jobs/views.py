from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Job_Position
from .serializers import Job_PositionSerializer
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import viewsets


class Job_PositionViewSet(viewsets.ModelViewSet):
	"""
		This viewset automatically provieds list, create, retrieve, update and destroy actions
	"""
	queryset 		   = Job_Position.objects.all()
	serializer_class   = Job_PositionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
		Automatically provides the deafult read-only operations resp. list and detail actions.
	"""
	queryset 		 = User.objects.all()
	serializer_class = UserSerializer