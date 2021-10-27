from django import forms
from pybo.models import Question

# 폼 상속


class QuestionForm(forms.ModelForm):
    # 메타 클래스 생성
    class Meta:
        # 모델 지정
        model = Question
        # 모델 필드 지정
        fields = ['subject', 'content']
        # 모델 속성 지정
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        # 모델 라벨명 지정
        labels = {
            'subject': '제목',
            'content': '내용',
        }
