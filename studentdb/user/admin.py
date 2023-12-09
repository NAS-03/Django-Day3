from django.contrib import admin
from .models import Profile
# Register your models here.

class adminView(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','mobile_no','grade','faculty']

admin.site.register(Profile,adminView)