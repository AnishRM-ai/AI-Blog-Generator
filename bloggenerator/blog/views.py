from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from .ai_blog_generator import generate_blog_content
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.content = generate_blog_content(post.title)
            post.save()
            return redirect('post_list')
        
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})