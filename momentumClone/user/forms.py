from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages = {
            'required' : '아이디를 입력해주세요.'
        },
        max_length=32, label = "아이디")
    password = forms.CharField(
        error_messages = {
            'required' : '비밀번호를 입력해주세요.'
        },
        widget = forms.PasswordInput, label = "비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            user = User.objects.get(userid = userid)
            if not user:
                self.add_error('userid', '일치하는 아이디가 없습니다.')
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 다릅니다.')
