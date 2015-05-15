import datetime
from datetime import timedelta
from django.db import models
from django import forms
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Job_Position(models.Model):
	job_name 	  = models.CharField('Job name', max_length = 300, blank = False)
	
	JOB_LOCATION  = (('KE', 'Kosice'), ('BA', 'Bratislava'))
	job_location  = models.CharField(choices = JOB_LOCATION, default = 'KE', max_length = 100)
	
	create_date   = models.DateField('Job created', default = timezone.now())
	start_date 	  = models.DateField('Start date', blank = False, null = False)
	
	CONTRACT_TYPE 	 = (('FT', 'Full time'),
					 	('PT', 'Part time'))
	contract_type 	 = models.CharField('Contract type:', choices = CONTRACT_TYPE, default = 'Full time', max_length = 20)

	job_description  = models.TextField('Job description')
	
	REQUIREMENTS     = (('1', 'University 1st degree'),
						('2', 'University 2nd degree'),
						('3', 'University 3rd degree'))
	job_requirements = models.CharField('Requirements', choices = REQUIREMENTS, default = 'University 2nd degree', max_length = 20)
	
	pc_requirements  = models.TextField('PC requirements')
	
	LANGUAGE 		 = (('EN-1', 'English - basic'),
						('EN-2', 'English advanced'),
						('DE-1', 'German - basic'),
						('DE-2', 'German - advanced'))
	language_requirements = models.CharField('Language requirements', choices = LANGUAGE, max_length = 20)
	
	other_requirements 	  = models.TextField('Other requirements')
	ness_info			  = models.TextField('Information about the company', default = "About Ness KDC.")

	owner = models.ForeignKey('auth.User', related_name = 'jobs', null = True)

	class Meta:
		ordering = ('create_date',)

	def __str__(self):
		return self.job_name

	def was_published_recently(self):
		return self.create_date >= datetime.date.today() - datetime.timedelta(days = 1)
	
	was_published_recently.admin_order_field = 'create_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Added recently?'
