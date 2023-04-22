from django import forms
from .models import Diary, Comment


class DiaryForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    mood = forms.CharField(
        label='오늘의 기분',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            },
        ),
    )
    image = forms.ImageField(
        label='사진 업로드',
        widget=forms.FileInput(
            attrs={
                'class': 'form-select',
            },
        ),
    )
    content = forms.CharField(
        label='일기 작성',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '오늘 하루는 어땠나요?',
            },
        ),
    )

    class Meta:
        model = Diary
        fields = ('title', 'mood', 'image', 'content',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '댓글을 작성하시오.',
            },
        ),
    )

    class Meta:
        model = Comment
        fields = ('content',)