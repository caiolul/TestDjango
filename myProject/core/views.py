from django.shortcuts import render, get_object_or_404, redirect
from myProject.core.models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.

'''Post.objects.get(pk=pk)'''


def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'index.html', {'posts': posts})


def post_pg(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'post_pg.html', {'posts': posts})


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
    return render(request, 'post_new_edit.html', {'form': form})



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
	return render(request, 'post_new_edit.html', {'form': form})

