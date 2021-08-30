from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TitleCustomAdmin(admin.ModelAdmin):
    list_display = ('title_de', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "ratings"


class TitleAdmin(TitleCustomAdmin, TranslationAdmin):
    pass


admin.site.register(PageTitleModel, TitleAdmin)
# *************************PageTitleModel*************************
