from django.contrib import admin
#from .models import User
from django.contrib.auth.models import User
from arriendo.models import Region,Commune,DepartmentType,Department

# Register your models here.
#admin.site.register(User)
admin.site.register(Region)
admin.site.register(Commune)
admin.site.register(DepartmentType)
admin.site.register(Department)
