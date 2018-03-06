from django.conf.urls import url
from . import views

app_name ='blog'

urlpatterns = [
	url(r'post$',views.post_list, name='blog_post'),
	url(r'create_blog$',views.create_blog, name='create_blog'),
	url(r'details/(?P<id>[0-9]+)/$', views.blog_detail, name="blog_detail"),
]
