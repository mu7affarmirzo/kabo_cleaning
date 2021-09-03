from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# *************************PageTitleModel*************************
class TitleCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Page Title"


class TitleAdmin(TitleCustomAdmin, TranslationAdmin):
    pass


admin.site.register(PageTitleModel, TitleAdmin)


# *************************StatisticsModel*************************
class StatisticsCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Statistics"


class StatisticsAdmin(StatisticsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(StatisticsModel, StatisticsAdmin)


# *************************MissionModel*************************
class MissionCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Missions"


class MissionAdmin(MissionCustomAdmin, TranslationAdmin):
    pass


admin.site.register(MissionModel, MissionAdmin)


# *************************CompanyMissionModel*************************
class CMissionCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Company Mission"


class CMissionAdmin(CMissionCustomAdmin, TranslationAdmin):
    pass


admin.site.register(CompanyMissionModel, CMissionAdmin)


# *************************TeamModel*************************
class TeamCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Our Team"


class TeamAdmin(TeamCustomAdmin, TranslationAdmin):
    pass


admin.site.register(TeamModel, TeamAdmin)
