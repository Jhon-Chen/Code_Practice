from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
# from django.template import loader, context
from django.shortcuts import render 

# 注意导包的路径
from django.core.urlresolvers import reverse 
from django.shortcuts import redirect
from django.http import HttpRequest 
from django.views.generic import View
from django.utils.decorators import method_decorator
# 注意导包的路径
from django.core.urlresolvers import reverse 

from .forms import BookForm

# Create your views here.

class BookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'form.html', {'form': form})
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid(): # 验证表单数据
            print(form.cleaned_data)  # 获取验证后的表单数据

            return HttpResponse("OK")
        else:
            return render(request, 'form.html', {'form': form})




"""
def index(request):
    # 1.获取模板
    template = loader.get_template('Users/index.html')
    # 2.定义上下文
    context = context(request,{'city': '北京'})
    # 3.渲染模板
    return HttpResponse(template.render(context))
"""

#或者这样子简写
def index(request):
    context = {'city': '北京',
               'adict':{
                   'name': '西游记',
                   'author': '吴承恩'
               },
                'alist': [1, 2, 3, 4, 5]
            }
    return render(request, 'index.html', context)


def index2(request):
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
    # request.session['you'] = 'lovely'
    # request = HttpRequest('you', 'tina')
    # request.session.get('name')
    return HttpResponse('OK')

def demo_view(request):
    # return HttpResponse('jhon tina', status=400)
    
    response = HttpResponse('jhon tina')
    response = HttpResponse('jhon tina')
    response.set_cookie('name', value='Tina_M', max_age=6000)
    response.status_code = 400
    response['jhon'] = 'tina'
    return response 

def demo_view2(request):
    return JsonResponse({'city': 'beijing', 'subject': 'python'})

    cookie1 = request.COOKIES.get('name')
    print(cookie1)
    return JsonResponse({'city': 'beijing', 'subject': 'python'})

def demo_view3(request):
    return redirect('http://47.100.200.127')



# def register(request):
   #  "处理注册信息"
    # 获取请求方法，判断是GET/POST请求
    # if request.method == 'GET':
        # 处理GET请求，返回注册页面
        # return render(request, 'register.html')
    # else:
        # 处理POST请求，实现注册逻辑
        # return HttpResponse('这里实现注册逻辑')
    


def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper



class RegisterView(View):
    """类视图，处理注册"""
    def get(self, request):
        """处理GET请求，返回注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('这里实现注册逻辑')


class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('OK')

    def post(self, request):
        print('post方法')
        return HttpResponse('OK')

# 为特定请求方法添加装饰器
class DemoView2(View):

    @method_decorator(my_decorator)
    def get(selt, request):
        print('get方法')
        return HttpResponse('OK')

    def post(self, request):
        print('post方法')
        return HttpResponse('OK')


# 使用name参数指明被装饰的方法
@method_decorator(my_decorator, name='post')
class DemoView3(View):
    def get(self, request):
        print('get就是这样')
        return HttpResponse('OK')

    def post(self, request):
        print('post不是你想要的')
        return HttpResponse('OK')


class MyDecoratorMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view

class DemoView4(MyDecoratorMixin, View):
    def get(self, request):
        print('get, 你想知道什么')
        return HttpResponse('OK')

    def post(self, request):
        print('post, 我想你需要平稳')
        return HttpResponse('OK')


def exm_view(request):
    print('view 视图被调用')
    return HttpResponse('OK')










































