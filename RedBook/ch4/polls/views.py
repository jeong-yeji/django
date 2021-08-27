from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Choice, Question
from django import forms
import logging

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


# 장고의 모든 폼 클래스는 is_valid() 메소드를 가짐.
# 모든 필드에 대해 유효성 검사 후, 모든 필드가 유효하면
# return True & 폼 데이터를 cleaned_data 속성에 넣음.
class NameForm(forms.Form):
    # TextInput
    your_name = forms.CharField(label="Your name", max_length=100)

    # Textarea
    # your_name = forms.CharField(label="Your name", max_length=100, widget=forms.Textarea)

    """
    렌더링 결과에는 <form> 태그나 submit 버튼이 없으므로 직접 넣어줘야됨
    <label for="your_name">Your name: </label>
    <input id="your_name" text="text" name="your_name" maxlength="100">
    """


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


def get_name(request):
    # POST 방식이면 데이터가 담긴 제출된 폼으로 간주
    if request.method == "POST":
        # request에 담긴 데이터로 클래스 폼 생성
        form = NameForm(request.POST)

        if form.is_valid():
            # 폼 데이터가 유효하면 데이터는 cleaned_data로 복사
            new_name = form.cleaned_data["name"]

            # 로직에 따라 추가적인 처리

            # 새로운 URL로 redirect
            return HttpResponseRedirect("/thanks")

    else:  # POST 방식이 아니면 (== GET 방식), 빈 폼을 사용자에게 보여줌
        form = NameForm()
        return render(request, "name.html", {"form": form})


# 로깅 설정 예시
# settings.py에서 설정된 로거를 취득함
logger = logging.getLogger("mylogger")


def my_view(request, arg1, arg):
    # 필요한 로직
    if bad_mojo:
        # ERROR 레벨의 로그 레코드 생성
        logger.error("Something went wrong!")


# 추가 로깅 메소드
# logger.log() : 원하는 로그레벨을 정해서 로그 메시지 생성
# logger.exception() : 익셉션 스택 트레이스 정보를 포함하는 ERROR 레벨의 로그 메시지 생성
