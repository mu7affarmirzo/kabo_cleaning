from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(PageTitleModel)
class TitleTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(StatisticsModel)
class StatisticsTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )

@register(MissionModel)
class MissionTranslationOptions(TranslationOptions):
    fields = (
        'header',
        'title',
        'text',
    )
