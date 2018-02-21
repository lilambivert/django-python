from django.conf.urls import url
from . import views


app_name ='bookz'

urlpatterns = [
    url(r'^home/$', views.home_view, name="home"),
    url(r'^purchase/(?P<id>[0-9]+)/$', views.purchase_view, name="purchase"),
    url(r'^login/$', views.login_view, name="login"),
]
