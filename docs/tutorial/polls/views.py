from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import context, loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from polls import models

# Create your views here.

"""
# view를 직접 만들어서 사용

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
    # 1
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # 2
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
"""


def vote(request, question_id):
    # 1
    # return HttpResponse("You're voting on question %s." % question_id)

    # 2
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didnt' select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )  # /polls/question.id/results/
        # reverse()의 사용으로 view에서 URL 하드 코딩 방지


# generic view 사용
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # return the last five published questions.
        # return Question.objects.order_by("-pub_date")[:5]

        # return the last five published questions(not future)
        # pub_date <= now인 Question을 포함하는 queryset
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    # URL에서 받을 기본키 값을 'pk'라고 기대하기 때문에 urls.py에서 변경
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        # excludes any questions that aren't published yet.
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
