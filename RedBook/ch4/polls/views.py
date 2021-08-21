from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Choice, Question

# Create your views here.


def index(request):
    # parameter : latest_question_list - pub_date 역순 정렬 후 최근 5개 객체
    latest_question_list = Question.objects.all().order_by("-pub_date")[:5]
    # parameter 넘겨주는 방식 : dictionary
    context = {"latest_question_list": latest_question_list}
    # render() : load template code, apply context variable, return HttpResponse
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # find object by pk=question_id from Question Model Class
    # 조건에 맞는 객체가 없음 => Http404 Exception
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여줌
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # When POST data is processed succesfully, return HttpResponseRedirect
        # reverse() : find URL string by URL pattern name
        # In general, URLconf names each line that maps URL string and view as URL pattern
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
