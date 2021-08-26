from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

"""
django.views.generic.View에서 as_view(), dispatch() 등을 제공
as_view()를 사용하면 클래스의 인스턴스를 생성하고,
그 인스턴스의 dispatch() 메소드로 request를 검사해 어떤 HTTP method로 요청되었는지 알아낸 다음
인스턴스 내에서 해당 이름을 갖는 메소드로 요청을 중계해줌
해당 메소드가 정의되어 있지 않으면 raise HttpResponseNotAllowed Exception
"""

"""
클래스형 뷰의 장점
1. Http method(GET, POST...)에 따른 처리 기능 구현 시, if 함수가 아닌 메소드명으로 구분하므로 코드 구조가 깔끔해짐
2. 다중 상속과 같은 객체 지향 기술 가능 -> 클래스형 제네릭 뷰 및 믹스인 클래스 등 이용 가능
   => 코드의 재사용성, 개발 생산성 증가
"""

# 클래스형 뷰
class MyView(View):
    def get(self, request):
        # write view logic
        return HttpResponse("result")

    # HEAD 요청 처리
    def head(self, *args, **kwargs):
        response = HttpResponse("")
        ## wirte view logic
        return response


# 함수형 뷰
# def my_view(request):
#     if request.method == 'GET':
#         # write view logic
#         return HttpResponse('result')
