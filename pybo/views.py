from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    # 질문 목록 내림차순(최신순)으로 조회
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # 'pybo/question_list.html' 템플릿 랜더링
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
