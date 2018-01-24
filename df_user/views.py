from django.shortcuts import render,redirect
from df_user.models import *

# Create your views here.


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    # 获取用户名密码邮箱.
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    # 将获取到的数据存进数据库
    # passport = PassPort()
    # passport.username = username
    # passport.password = password
    # passport.email = email
    # passport.save()
    # 普通写法 以下是简写方式
    print(username)
    print(password)
    print(email)
    # passport = PassPort(username=username, password=password, email=email)
    # passport.save()
    PassPort.objects.add_one(username=username, password=password, email=email)
    return redirect('/user/login/')
