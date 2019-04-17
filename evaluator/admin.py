from django.contrib import admin
from .models import Company, Company_Field, User, User_Field

# Register your models here.
admin.site.register(Company)
admin.site.register(Company_Field)
admin.site.register(User)
admin.site.register(User_Field)