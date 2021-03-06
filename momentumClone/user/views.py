from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm

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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk = user_id)
        return HttpResponse(user.username + '님, 환영합니다')
    else:
        res_data = {}
        res_data['error'] = '일치하는 아이디가 없습니다'
        return render(request, 'login.html', res_data)

    
    return HttpResponse('Home')
