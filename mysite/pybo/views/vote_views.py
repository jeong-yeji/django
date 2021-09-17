from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, resolve_url

from ..models import Comment, Question, Answer

## 추천 관리 ##

# 질문 추천
@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else: # ManyToManyField => add()
        question.voter.add(request.user)
        # ManyToManyField는 중복X => 여러번 추천해도 추천 수는 증가하지 않음
    return redirect('pybo:detail', question_id=question.id)


# 답변 추천
@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id=answer.question.id), answer_id))


# 댓글 추천
@login_required(login_url='common:login')
def vote_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        comment.voter.add(request.user)
    
    if comment.question:
        return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', question_id=comment.question.id), comment_id))
    else: # if comment.answer
        return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', question_id=comment.answer.question.id), comment_id))
