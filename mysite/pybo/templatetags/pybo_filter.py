from django import template

register = template.Library()

# add는 음수의 인자를 받을 수 있지만 변수는 받을 수 없음
# >> 변수를 사용하도록 sub filter 생성
@register.filter
def sub(value, arg):
    return value - arg