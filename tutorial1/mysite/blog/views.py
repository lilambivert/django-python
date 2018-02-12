#from django import forms
from .forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
        title = request.POST['title']
        author = request.POST['author']
        body = request.POST['body']
        q = User.objects.get(id=int(author))
        post = Post(title=title, author=q, body=body)
        post.save()

        return redirect('/blog/post')
    else:
        userslist = User.objects.all()
        users = {
            'users':userslist
        }

        return render(request, 'blog/blogpost.html', users)

def blog_detail(request, id):
    blog = Post.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)

    post = get_object_or_404(Post, id=id)
    if(request.method == 'POST'):
        formz = CommentForm(request.POST)
        if formz.is_valid():
            comment = formz.save(commit=False)
            comment.blog = blog
            comment.post = request.user.get_username()
            comment.save()
            return redirect('blog/post')
    else:
        formz = CommentForm()
    return render(request, 'blog/blog_details.html', {'blog':blog, 'comments':comments, 'formz' : formz})
