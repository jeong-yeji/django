from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

## 기본 관리 ##

def index(request):
    # parameter
    page = request.GET.get('page', '1')  # page, 기본값 1
    kw = request.GET.get('kw', '')       # 검색어

    # 검색
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            # Q() : OR 조건으로 데이터 조회
            # contains vs icontains : 대소문자 구별O vs 구별X
            Q(subject__icontains=kw) |                  # 제목
            Q(content__icontains=kw) |                  # 내용
            Q(author__username__icontains=kw) |         # 질문 글쓴이
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이
        ).distinct() # 중복 제거

    # pagination
    paginator = Paginator(question_list, 10) # 10 questions per page
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
