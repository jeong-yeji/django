from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

# StackedInline : 리스트 형식
# TabularInline : 테이블 형식
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 필드 순서 변경
    # fields = ["pub_date", "question_text"]

    # 필드 분리하여 표시, 필드 접기
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # Choice 모델 클래스 같이 보기
    list_display = ("question_text", "pub_date")  # 레코드 리스트 컬럼 지정
    list_filter = ["pub_date"]  # 필터 사이드 바 추가
    search_fields = ["question_text"]  # 검색 박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
