from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from post.forms import CategoryForm, CommentForm, PostForm
from post.models import Category, Post


# Create your views here.


def index(request):
    authors = User.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'authors': authors,
        'categories': categories,
        'posts': posts,
        'form': CategoryForm(),
        'post_form': PostForm()
    }

    return render(request, 'post/index.html', ctx)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    return redirect('index')


def author(request, id):
    author = User.objects.get(pk=id)
    posts = author.posts.all()

    ctx = {
        'author': author,
        'posts': posts
    }

    return render(request, 'post/author.html', ctx)


def category(request, id):
    category = Category.objects.get(pk=id)
    posts = category.posts.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'category': category,
        'posts': posts,
        'form': CategoryForm()
    }

    return render(request, 'post/category.html', ctx)


def post(request, id):
    post = Post.objects.get(pk=id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    ctx = {
        'post': post,
        'comments': comments,
        'form': CommentForm()
    }

    return render(request, 'post/post.html', ctx)