from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    # User 모델은 django 앱에서 제공하는 사용자 모델
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # Question 모델 조회시 id값 대신 제목을 표시하도록 매서드 추가
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Question 모델과 연결 및 삭제연동
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
