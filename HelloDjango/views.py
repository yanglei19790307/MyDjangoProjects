
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status


def HelloWorld(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'HelloWord.html')


def Weather(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'Weather.html')

def Home(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'home.html')

def Login(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'Login.html')

def LoginHandle(request):
    uerID= request.GET['userID']
    ##request.session['userID'] = uerID

    if request.session.get('userID', False):
        return HttpResponse('您已经登录，登录名为' + request.session['userID']  );
    else:
        request.session['userID'] = uerID
        return HttpResponse('您刚登录，您的用户名为:' + uerID)


def Restful(request):
    content = {'msg': 'SUCCESS'}
    # 返回自定义请求内容content,200状态码
    return JsonResponse(data=content, status=status.HTTP_200_OK)


def Redirection(request):
    return HttpResponseRedirect('http://www.baidu.com')

def Index(request):
    return HttpResponse('this is index page')

def Add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))