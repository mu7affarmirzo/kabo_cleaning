from modeltranslation.translator import translator, TranslationOptions, register
from .models import *

@register(LeadersModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'position')
