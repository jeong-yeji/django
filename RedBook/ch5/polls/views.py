from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.models import Choice, Question
import logging

# Create your views here.

# __name__ : 모듈 경로를 담고 있는 파이썬 내장 변수
# module path of views.py == polls.views == logger obj name
logger = logging.getLogger(__name__) # polls.views logger obj 취득

# Class-based View
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return the last five published questions.
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# Function-based View
def vote(request, question_id):
    # DEBUG 수준의 로드 레코드 생성
    logger.debug("vote().question_id: %s" % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))