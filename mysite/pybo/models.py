from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='category_question')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    voter = models.ManyToManyField(User, related_name='voter_question', blank=True)
    view_count = models.IntegerField(blank=True, default=0)
    is_notice = models.BooleanField(blank=True, default=False)
    # author와 voter가 모두 User 모델을 참조하므로
    # User.question_set과 같이 User 모델을 통해 Question 데이터에 접근할 경우 어떤걸 참조할지 지정해야됨
    # 특정 사용자가 작성한 질문을 얻는 코드 : some_user.author_question.all()
    # 특정 사용자가 추천한 질문을 얻는 코드 : some_user.voter_question.all()


    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_comment')