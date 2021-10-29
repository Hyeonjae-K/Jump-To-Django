from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question


def index(request):
    # URL에서 요청한 페이지 가져옴(default=1)
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')
    # 정렬
    if so == 'recommend':
        # 추천 수 내림차순, 최신순
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        # 답변 개수 내림차순, 최신순
        question_list = Question.objects.annotate(num_answer=Count(
            'answer')).order_by('-num_answer', '-create_date')
    else:
        # 질문 목록 내림차순(최신순)으로 조회
        question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(Q(subject__icontains=kw) | Q(content__icontains=kw) | Q(
            author__username__icontains=kw) | Q(answer__author__username__icontains=kw)).distinct()
    # 페이지당 15개씩 나눔
    paginator = Paginator(question_list, 15)
    # 요청 페이지의 질문 반환
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    # 'pybo/question_list.html' 템플릿 랜더링
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
