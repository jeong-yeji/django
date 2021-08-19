import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 1 : 날짜가 미래인 경우 True를 반환함
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        # 2 : 버그 수정 - 날짜가 과거일 때만 True를 반환하도록 수정
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # 출력 설정
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    quuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)