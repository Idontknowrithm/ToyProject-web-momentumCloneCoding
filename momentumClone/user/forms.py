from django import forms
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ObjectDoesNotExist

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
            try:
                user = User.objects.get(userid = userid)
                if not check_password(password, user.password):
                    self.add_error('password', '비밀번호가 다릅니다.')
                else:
                    self.user_id = user.id
            except ObjectDoesNotExist:
                self.add_error('userid', '일치하는 아이디가 없습니다.')

class RegisterForm(forms.Form):
    userid = forms.CharField(
        error_messages = {
            'required' : '아이디를 입력해주세요.'
        },
        max_length=32, label = "아이디"
    )
    username = forms.CharField(
        error_messages = {
            'required' : '이름을 입력해주세요.'
        },
        max_length=32, label = "이름"
    )
    useremail = forms.EmailField(
        error_messages = {
            'required' : '이메일을 입력해주세요.'
        },
        max_length=32, label = "이메일"
    )
    password = forms.CharField(
        error_messages = {
            'required' : '비밀번호를 입력해주세요.'
        },
        max_length=32, widget = forms.PasswordInput, label = "비밀번호"
    )
    re_password = forms.CharField(
        error_messages = {
            'required' : '비밀번호를 다시 확인해주세요.'
        },
        max_length=32, widget = forms.PasswordInput, label = "비밀번호 확인"
    )
    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        username = cleaned_data.get('username')
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if userid and username and useremail and password and re_password:
            if not check_password(password, re_password):
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
            else:
                user = User(
                userid = userid,
                username = username,
                useremail = useremail,
                password = make_password(password)
                )
                user.save()
            
