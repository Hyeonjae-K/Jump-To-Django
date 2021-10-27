from typing import ContextManager
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer


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


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # POST로 전송된 데이터의 'content'를 읽어 Answer 모델에 저장
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    Answer(question=question, content=request.POST.get(
        'content'), create_date=timezone.now()).save()
    return redirect('pybo:detail', question_id=question.id)
