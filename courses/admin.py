from django.contrib import admin
from courses.models import Course, Student

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)