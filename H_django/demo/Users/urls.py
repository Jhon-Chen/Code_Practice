from django.conf.urls import url 
from . import views

urlpatterns = [
    # url(路径，视图) 使用正则表达式的方式    
    url(r'^index/$', views.index, name='index'),
    # 路由解析的顺序是由上至下，有可能上面的路由会屏蔽下面的路由
    url(r'^say/$',views.say, name='say'),
    url(r'^sayhello', views.sayhello),
    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    url(r'^qs/', views.qs),
    url(r'^get_headers/$', views.get_headers),
    url(r'^demo_view/$', views.demo_view),
    url(r'^demo_view2/$', views.demo_view2)
]
