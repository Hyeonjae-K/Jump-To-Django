from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    # 요청이 'POST'일 경우
    if request.method == 'POST':
        # request.POST에 전달된 데이터가 각 속성에 자동으로 저장
        form = QuestionForm(request.POST)
        # 데이터가 유효할 경우
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장
            question.author = request.user
            question.create_date = timezone.now()
            question.save()  # 실제 저장
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 작성자가 아닐 경우
    if request.user != question.author:
        # non-field error 발생
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    # 요청이 'POST'일 경우(저장)
    if request.method == 'POST':
        # instance(question)값을 request.POST 값으로 대체
        form = QuestionForm(request.POST, instance=question)
        # 유효할 경우 저장(DB 반영)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')
