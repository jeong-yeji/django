from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import context, loader
from .models import Question

# Create your views here.


def index(request):
    # 1
    # return HttpResponse("Hello, world. You're at the polls index.")

    # 2
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 3
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 4 : render()를 이용한 3 변형
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # dict type value that matches variable name in template and python object
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)  # request, template, (context)


def detail(request, question_id):
    # 1
    # return HttpResponse("You're looking at question %s." % question_id)

    # 2 : raise 404 error
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    # 3 : raise 404 error with shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    # ObjectDoesNotExist > get_object_or_404(), Http404를 사용하는 이유
    # 모델 게층을 뷰 계층에 연결하는 방법이기 때문


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)