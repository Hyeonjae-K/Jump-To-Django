from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # 검색기능 추가
    search_field = ['subject']


# admin 페이지에 Question 모델 등록
admin.site.register(Question, QuestionAdmin)
