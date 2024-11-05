from django.contrib import admin
# 3
from .models import College, Program, Organization, Student, OrgMember

# Register your models here.
#2
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")
    search_fields = ("prog_name", "college__college_name")

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name","college")
    search_fields = ("name", "college__college_name",)

# 4
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname",
                    "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)

# 5
@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "member_program", "organization", "date_joined",)
    search_fields = ("student__lastname", "student__firstname",)

    def member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None