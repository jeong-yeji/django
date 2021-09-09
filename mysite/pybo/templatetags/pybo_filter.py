import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# add는 음수의 인자를 받을 수 있지만 변수는 받을 수 없음
# >> 변수를 사용하도록 sub filter 생성
@register.filter
def sub(value, arg):
    return value - arg


# markdown filter
# nl2br : 줄바꿈문자를 <br> 태그로 바꿔줌 >> 엔터 한번만 눌러도 줄바꿈으로 인식
# fenced_code : 마크다운의 소스 코드 표현
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))