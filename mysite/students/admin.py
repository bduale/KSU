from django.contrib import admin
from . models import Student

# Register your models here.
#class StudentsAdmin(admin.model.admin):
#    list_display=[student_number, first_name, last_name]
admin.site.register(Student)
