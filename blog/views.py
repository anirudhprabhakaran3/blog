from django.shortcuts import render,get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

from .models import Post, Message, Category
from .forms import PostForm, MessageForm

# Create your views here.
def post_list(request):
    posts_list = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    message = Message.objects.all().order_by('-id')
    heading = "Posts"
    args = {
    'posts':posts,
    'messages':message,
    "heading" : heading
    }
    return render(request, 'blog/post_list.html', args)

def search(request):
    posts = Post.objects.all().order_by('-published_date')
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(content__icontains=query) |
            Q(batch__icontains=query)
            ).distinct()
    message = Message.objects.all().order_by('-id')
    args = {
    'posts':posts,
    'messages':message
    }
    return render(request, 'blog/search.html', args)

def home(request):
    message = Message.objects.all().order_by('-id')
    x = Post.objects.all()
    if x:
        firstpost = Post.objects.all().order_by('-published_date')[0]
        posts = Post.objects.all().order_by('-published_date')[1:4]
    else:
        posts = []
        firstpost = []
    args = {
    'messages' : message,
    'firstpost' : firstpost,
    'posts' : posts,
    }
    return render(request, 'blog/home.html', args)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    message = Message.objects.all().order_by('-id')
    args = {
        'post' : post,
        'messages' : message,
    }
    return render(request, 'blog/post_detail.html',args)

def categories_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    try:
        posts = Post.objects.filter(category=pk)
    except Post.DoesNotExist:
        posts = None
    message = Message.objects.all().order_by('-id')
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    args = {
        'category': category,
        'posts': posts,
        'message': message,
    }
    return render(request, 'blog/categories_detail.html', args) 

def about(request):
    message = Message.objects.all().order_by('-id')
    args = {
     'messages' : message,
    }
    return render(request, 'blog/about.html', args)

def categories(request):
    categories = Category.objects.all()
    message = Message.objects.all().order_by('-id')
    args = {
        'categories' : categories,
        'messages' : message,
    }
    return render(request, 'blog/categories.html', args)

@staff_member_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    message = Message.objects.all().order_by('-id')
    args = {
        'form' : form,
        'messages': message,
    }
    return render(request, 'blog/post_edit.html', args)

@staff_member_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    message = Message.objects.all().order_by('-id')
    args = {
        'form' : form,
        'messages': message,
    }
    return render(request, 'blog/post_edit.html', args)