from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    # URL에서 요청한 페이지 가져옴(default=1)
    page = request.GET.get('page', '1')
    # 질문 목록 내림차순(최신순)으로 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이지당 15개씩 나눔
    paginator = Paginator(question_list, 15)
    # 요청 페이지의 질문 반환
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    # 'pybo/question_list.html' 템플릿 랜더링
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


# 로그인되지 않은 상태에서 함수 호출시 'login' 페이지로 이동
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # 로그인 계정 저장
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # POST로 전송된 데이터의 'content'를 읽어 Answer 모델에 저장
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    Answer(question=question, content=request.POST.get(
        'content'), create_date=timezone.now()).save()
    return redirect('pybo:detail', question_id=question.id)


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


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)
