from django.shortcuts import render, get_object_or_404
from myProject.core.models import Post
from django.utils import timezone

# Create your views here.

'''Post.objects.get(pk=pk)'''

def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'index.html', {'posts': posts})

def post_pg(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'post_pg.html', {'posts': posts})