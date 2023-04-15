from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    profile_image = forms.ImageField(
        label='프로필 사진',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com',
            },
        ),
    )
    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            arrts={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영문자/특수문자/숫자의 조합으로 8자 이상 16자 이하'
            },
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'profile_image', 'email', 'last_name', 'first_name', 'birthday', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    profile_image = forms.ImageField(
        label='프로필 사진',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com',
            },
        ),
    )
    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            arrts={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )
    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'profile_image', 'email', 'last_name', 'first_name', 'birthday',)


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    new_password1= forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    new_password2 = forms.CharField(
        label='새 비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )