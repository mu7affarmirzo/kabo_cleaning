from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin

# this is for ratingData
class LeadersCustomAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_de', 'name_ru')
    class Meta:
        verbose_name = "Leaders"
class LeadersAdmin(LeadersCustomAdmin, TranslationAdmin):
    pass
admin.site.register(LeadersModel, LeadersAdmin)

