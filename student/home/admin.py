from django.contrib import admin

# Register your models here.
from .models import Student
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name',
        'dob' ,
        'physics_marks',
        'chemistry_marks',
        'maths_marks',
        'cs_marks',
        'total_marks',
        'percentage'
        ]