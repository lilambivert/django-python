from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required

#Lists the 5 most recent posts
def post_list(request):
	posts = Post.objects.all()[:5]

	context = {
		'posts':posts
	}

	return render(request, 'blog/base2.html', context)

@login_required
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

def blog_detail(request, title):
	blog = Post.objects.get(id=title)
	return render(request, 'blog/blog_details.html', {'blog':blog}) 

