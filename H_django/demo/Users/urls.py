from django.conf.urls import url 
from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns = [
    # url(路径，视图) 使用正则表达式的方式    
    url(r'^index/$', views.index),
    # 路由解析的顺序是由上至下，有可能上面的路由会屏蔽下面的路由
    url(r'^say/$',views.say, name='say'),
    url(r'^sayhello', views.sayhello),
    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    url(r'^qs/', views.qs),
    url(r'^get_headers/$', views.get_headers),
    url(r'^demo_view/$', views.demo_view),
    url(r'^demo_view2/$', views.demo_view2),
    url(r'^demo_view2/$', views.demo_view2),
    url(r'^demo_view3/$', views.demo_view3),
    # url(r'^register/$', views.register),
    
    # 类视图：注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 类视图装饰
    url(r'^demo/$', views.my_decorator(views.DemoView.as_view())),
    url(r'^demo4/$', views.DemoView2.as_view()),
    url(r'^demo5/$', views.DemoView3.as_view()),
    url(r'^demo6/$', views.DemoView4.as_view()),
    url(r'^exm/$', views.exm_view),
    # url(r'^books/$', views.BooksAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所有路由信息追加到Django路由列表中






