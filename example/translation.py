from modeltranslation.translator import register, TranslationOptions
from .models import Course


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('description', 'name', 'short_description')
