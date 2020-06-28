from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster Admin Area'


# for presenting the list of
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 3 extra fields


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
