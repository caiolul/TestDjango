from django.shortcuts import render, get_object_or_404, redirect
from myProject.core.models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
#Tela inicial

def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'content.html', {'posts': posts})


def post_pg(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_pg.html', {'posts': posts})

#Area de crianção e edição de posts

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        post.pub_date = timezone.now()
	        post.save()
        return redirect('post_pg', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_new_edit.html', {'form': form})


def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.pub_date = timezone.now()
			post.save()
			return redirect('post_pg', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post/post_new_edit.html', {'form': form})

#Registro e login de users

def register_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'login/register_pg.html', {'form':form})


def login_form(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login/login_pg.html', {'form':form})

def logout_form(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')

# Search bar

def search(request):
    pass
