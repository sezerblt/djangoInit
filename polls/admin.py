from django.contrib import admin

from .models import Question,Choice


class ChoiceInline(admin.StackedInline):#(admin.TabularInLine)
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        ('Soru olustur', {'fields': ['question_text']}),
        ('Yayinlama',   {'fields': ['pub_date']}),
    ]
    list_filter=['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
"""
class ChoiceAdmin(admin.ModelAdmin):
    #fields = ['question', 'choice_text','votes']
    fieldsets = [
        ('Soru Getir', {'fields': ['question']}),
        ('Yayinlama', {'fields': ['choice_text','votes']}),
    ]
"""

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)