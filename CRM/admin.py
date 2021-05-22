from django.contrib import admin
from.models import *

    
class AccusedAdmin(admin.ModelAdmin):
    search_fields=['name_accused']
    list_display=['name_accused','felony_accused','age_accused','condemnation_accused','address_accused',]
class EmployesAdmin(admin.ModelAdmin):
    search_fields=['name_employ']
    list_display=['name_employee','job_name','age_employees','Salary_employees','address_employees']
    
# Register your models here.
admin.site.register(Accused,AccusedAdmin)
admin.site.register(Employe,EmployesAdmin)
admin.site.register(FrontManager)