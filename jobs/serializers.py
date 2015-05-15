from django.forms import widgets
from rest_framework import serializers
from .models import Job_Position
from django.contrib.auth.models import User

class Job_PositionSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Job_Position 	#we're returning the Job_Position id, so I have a refenrence to it if I want to update or delete it.
		fields = ('id', 'owner', 'job_name', 'job_location', 'create_date', 'start_date', 'contract_type', 'job_description', 'language_requirements')
		#fileds I wanted to use form my Job_Position model

class UserSerializer(serializers.ModelSerializer):
    jobs = serializers.PrimaryKeyRelatedField(many=True, queryset=Job_Position.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'jobs')
