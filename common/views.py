from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    # 만약 요청이 'POST'일 경우
    if request.method == 'POST':
        form = UserForm(request.POST)
        # 이메일 및 비밀번호 등 입력 검증
        if form.is_valid():
            # 사용자 저장
            form.save()
            # 'username' 입력값 반환
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 사용자명과 비밀번호 검증
            user = authenticate(usrename=username, password=raw_password)
            # 회원가입 후 자동 로그인
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
