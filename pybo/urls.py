from django.urls import path
from . import views

urlpatterns = [
    # ''로 요청이 들어올 경우 views.py 파일의 index 함수 호출
    path('', views.index),
    path('<int:question_id>/', views.detail)
]
