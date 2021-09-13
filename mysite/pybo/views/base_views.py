from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question

## 기본 관리 ##

def index(request):
    # parameter
    page = request.GET.get('page', '1')  # page, 기본값 1
    kw = request.GET.get('kw', '')       # 검색어
    so = request.GET.get('so', 'recent') # 정렬 기준

    # 정렬
    # annotate() : 임의의 필드를 임시로 추가해주는 함수 > filter(), order_by()에서 사용 가능
    # order_by의 기준이 여러개인 경우, 첫번째 항목부터 우선순위를 매김
    if so == 'recommend': # 추천순
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular': # 인기순 : 답변이 많이 달린 순으로
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # default: 최신순
        question_list = Question.objects.order_by('-create_date')

    # 검색
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

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    question.view_count += 1
    question.save()
    return render(request, 'pybo/question_detail.html', context)
