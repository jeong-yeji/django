from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question, Category, Answer, Comment

## 기본 관리 ##

def index(request):
    3/0
    # parameter
    page = request.GET.get('page', '1')   # page, 기본값 1
    kw = request.GET.get('kw', '')        # 검색어
    so = request.GET.get('so', 'recent')  # 정렬 기준
    cate = request.GET.get('cate', 'all')

    notice_list = Question.objects.filter(is_notice=True)
    question_list = Question.objects.filter(is_notice=False)

    # category
    if cate != 'all':
        question_list = question_list.filter(category__name=cate)

    # 정렬
    # annotate() : 임의의 필드를 임시로 추가해주는 함수 > filter(), order_by()에서 사용 가능
    # order_by의 기준이 여러개인 경우, 첫번째 항목부터 우선순위를 매김
    if so == 'recommend': # 추천순
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular': # 인기순 : 답변이 많이 달린 순으로
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # default: 최신순
        question_list = question_list.order_by('-create_date')

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

    # category
    category_list = Category.objects.all()

    context = {'question_list': page_obj, 'notice_list': notice_list, 'page': page, 'kw': kw, 'so': so, 'category_list': category_list, 'cate': cate}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # parameters
    page = request.GET.get('page', '1')
    so = request.GET.get('so', 'recommend')
    question = get_object_or_404(Question, pk=question_id)

    # 조회수
    question.view_count += 1
    question.save()

    # 답변 정렬
    answer_list = Answer.objects.filter(question=question).annotate(num_voter=Count('voter'))
    if so == 'recommend':
        answer_list = answer_list.order_by('-num_voter', 'create_date')
    else: # recent, 시간순
        answer_list = answer_list.order_by('create_date', '-num_voter')

    # 답변 페이징
    paginator = Paginator(answer_list, 5)
    page_obj = paginator.get_page(page)
    
    context = {'question': question, 'answer_list': page_obj, 'page': page, 'so': so}
    return render(request, 'pybo/question_detail.html', context)


def recent(request):
    # parameter
    answer_list = Answer.objects.all().order_by('-create_date')
    comment_list = Comment.objects.all().order_by('-create_date')

    context = {'answer_list': answer_list, 'comment_list': comment_list}
    return render(request, 'pybo/recent_list.html', context)