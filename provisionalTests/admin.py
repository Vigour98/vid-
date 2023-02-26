from django.contrib import admin
from .models import Prov_Questions, Answers

class AnswersInline(admin.StackedInline):
    model = Answers
    extra = 0


class Prov_QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        (None, {'fields':['Q_Image']}),
        (None, {'fields':['answer']}),
        (None, {'fields':['category']}),
        
    ] 

    inlines = [AnswersInline] 

admin.site.register(Prov_Questions, Prov_QuestionsAdmin)       