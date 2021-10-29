from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    # User 모델은 django 앱에서 제공하는 사용자 모델
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # N:N 관계
    voter = models.ManyToManyField(User, related_name='voter_question')

    # Question 모델 조회시 id값 대신 제목을 표시하도록 매서드 추가
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_answer')
    # Question 모델과 연결 및 삭제연동
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, null=True, blank=True, on_delete=models.CASCADE)
