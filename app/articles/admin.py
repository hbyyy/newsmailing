

# Register your models here.
from django.contrib import admin

from articles.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
