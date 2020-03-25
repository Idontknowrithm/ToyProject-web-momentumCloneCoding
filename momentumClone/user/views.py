from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        userid = request.POST['userid']
        username = request.POST['username']
        useremail = request.POST['useremail']
        password = request.POST['password']
        re_password = request.POST['re_password']

        res_data = {}
        if not (userid and username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                userid = userid,
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            user.save()

        return render(request, 'register.html', res_data)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        userid = request.POST.get('userid', None)
        password = request.POST.get('password', None)