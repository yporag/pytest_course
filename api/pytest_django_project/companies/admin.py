from django.contrib import admin
from api.pytest_django_project.companies.models import Company

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
