from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question


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
