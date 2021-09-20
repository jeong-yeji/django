from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from allauth.socialaccount.models import SocialAccount

from django.contrib.auth.models import User
from pybo.models import Question, Answer, Comment

@login_required(login_url='common:login')
def base(request, user_id):
    # parameter
    user = get_object_or_404(User, pk=user_id)
    is_social = SocialAccount.objects.filter(user=user).exists()
    
    context = {'user': user, 'is_social': is_social, 'profile_type': 'base'}
    return render(request, 'common/profile_base.html', context)


@login_required(login_url='common:login')
def question(request, user_id):
    # parameter
    user = get_object_or_404(User, pk=user_id)
    page = request.GET.get('page', '1')
    so = request.GET.get('so', 'recent')

    # 정렬
    question_list = Question.objects.filter(author=user)
    if so == 'recommend':
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    else: # recent
        question_list = question_list.order_by('-create_date')

    # pagination
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {'user': user, 'profile_type': 'question', 'question_list': page_obj, 'page': page}
    return render(request, 'common/profile_question.html', context)


@login_required(login_url='common:login')
def answer(request, user_id):
    # parameter
    user = get_object_or_404(User, pk=user_id)
    page = request.GET.get('page', '1')
    so = request.GET.get('so', 'recent')

    # 정렬
    answer_list = Answer.objects.filter(author=user)
    if so == 'recommend':
        answer_list = answer_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    else: # recent
        answer_list = answer_list.order_by('-create_date')

    # pagination
    paginator = Paginator(answer_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {'user': user, 'profile_type': 'answer', 'answer_list': page_obj, 'page': page}
    return render(request, 'common/profile_answer.html', context)


@login_required(login_url='common:login')
def comment(request, user_id):
    # parameter
    user = get_object_or_404(User, pk=user_id)
    page = request.GET.get('page', '1')
    so = request.GET.get('so', 'recent')

    # 정렬
    comment_list = Comment.objects.filter(author=user)
    if so == 'recommend':
        comment_list = comment_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    else: # recent
        comment_list = comment_list.order_by('-create_date')

    # pagination
    paginator = Paginator(comment_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {'user': user, 'profile_type': 'comment', 'comment_list': page_obj, 'page': page}
    return render(request, 'common/profile_comment.html', context)
