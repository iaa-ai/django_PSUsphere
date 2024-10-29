from django.contrib import admin

# Register your models here.
#2
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)
admin.site.register(Student)
admin.site.register(OrgMember)