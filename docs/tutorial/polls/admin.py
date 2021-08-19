from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# StackedInline : list형태로 쭉 나타냄
# TabularInline : 좀 더 간결하게 표 형식으로 나타냄
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 슬롯 3개로 설정


class QuestionAdmin(admin.ModelAdmin):
    ## ADD QUESTION PAGE ##
    # fields = ["pub_date", "question_text"]  # 필드 표시 순서 지정
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]  # 필드가 많은 경우 fieldset으로 폼 분할
    inlines = [ChoiceInline]

    ## QUESTION LIST PAGE ##
    # Questions 리스트에서 표시할 것
    # 임의의 메소드(was_published_recetly)에 의한 출력 제외 정렬 가능
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]  # 필터링 기능 - 필드 유형에 따라 필터 옵션 제공
    search_fields = ["question_text"]  # 검색창 기능 (LIKE 쿼리 이용함)


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)