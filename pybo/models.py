from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # Question 모델 조회시 id값 대신 제목을 표시하도록 매서드 추가
    def __str__(self):
        return self.subject


class Answer(models.Model):
    # Question 모델과 연결 및 삭제연동
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
