from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    # ''로 요청이 들어올 경우 views.py 파일의 index 함수 호출
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/',
         views.answer_create, name='answer_create')
]
