from django.contrib import admin
from organization.models import InvestorType, InvestmentStage

# Register your models here.

admin.site.register(InvestorType)

admin.site.register(InvestmentStage)
