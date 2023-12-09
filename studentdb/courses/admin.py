from django.contrib import admin
from .models import Courses
# Register your models here.

class courseView(admin.ModelAdmin):
    list_display=['id','course_name','instructor','course_length']

admin.site.register(Courses,courseView)