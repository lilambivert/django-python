from django.shortcuts import render, redirect
#from django.shortcuts import render_to_response
from django.contrib.auth.models import User
#from django.contrib. import auth
#from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from .models import Post

def post_list(request):
	posts = Post.objects.all()[:10]

	context = {
		'posts':posts
	}

	return render(request, 'blog/base2.html', context)

def create_blog(request):

	if(request.method == 'POST'):
		print "request.POST", request.POST
		title = request.POST['title']
		author = request.POST['author']
		body = request.POST['body']
		q = User.objects.get(id=int(author))			
		post = Post(title=title, author=q, body=body)
		post.save()

		return redirect('/blog/post')
	else:
		print "request.user", request.user.id
		userslist = User.objects.all()
		users = {
		      'users':userslist
		}

		return render(request, 'blog/blogpost.html', users)
