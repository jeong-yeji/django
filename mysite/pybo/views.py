from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Question 모델을 통한 데이터 저장
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    # Answer 모델을 통한 데이터 저장
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()

    return redirect('pybo:detail', question_id=question.id)