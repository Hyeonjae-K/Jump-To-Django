from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    # 뷰 함수를 따로 만들지 않고 LoginView 사용(템플릿 지정)
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login')
]
