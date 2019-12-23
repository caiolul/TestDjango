from django.shortcuts import render
from django.http import HttpResponse
from myProject.core.models import Post
from django.utils import timezone

# Create your views here.


def index(request):
    post = Post.objects.filter(
        pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'index.html', {'post': post})
