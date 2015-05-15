from django.contrib import admin
from .models import Job_Position


class Jobs_Admin(admin.ModelAdmin):
	fieldsets = [(None,               			   {'fields': ['job_name']}),
				 ('Informacie o pracovnom mieste', {'fields': ['job_location', 'start_date', 'contract_type']}),
				 (None, 						   {'fields': ['job_description']}),
				 ('Poziadavky na zamestnanca', 	   {'fields': ['job_requirements', 'language_requirements', 'pc_requirements']}),
				 ('O spolocnosti Ness', 		   {'fields': ['ness_info']}),
				 (None, 						   {'fields': ['create_date']}),
				 ('Owner', 						   {'fields': ['owner']})
				]
	list_display = ('job_name', 'create_date', 'was_published_recently', 'owner')
	list_filter  = ['create_date']
	# raw_id_fields = ('owner',)

admin.site.register(Job_Position, Jobs_Admin)
# Register your models here.


