from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse


# 注意导包的路径
from django.core.urlresolvers import reverse 

# Create your views here.

def index(request):
    """视图：
    request：用于接收请求request对象
    return：响应对象"""
    
    return HttpResponse('Hello World!')

def say(request):
    url = reverse("Users:index")
    # 返回 /Users/index 
    print(url)
    return HttpResponse("say page")

def sayhello(request):
    return HttpResponse("say hello page")

def weather(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('OK')

# /qs/?a=1&b=2&a=3

def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')

# def get_body(request):
    # a = request.POST.get('a')
    # b = request.POST.get('b')
    # alist = request.POST.getlist('a')
    # print(a)
    # print(b)
    # print(alist)

    # return HttpResponse('OK')

def get_headers(request):
    print(request.META['CONTENT_TYPE'])
    return HttpResponse('OK')

def demo_view(request):
    # return HttpResponse('jhon tina', status=400)
    
    response = HttpResponse('jhon tina')
    response.status_code = 400
    response['jhon'] = 'tina'
    return response 

def demo_view2(request):
    return JsonResponse({'city': 'beijing', 'subject': 'python'})







