from django.contrib import admin
from .models import Question, Answer, Category, Comment

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)