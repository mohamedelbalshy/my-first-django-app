from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    # return HttpResponse('HELLO FROM POSTS')
    posts = Post.objects.all()[:10]

    context = {
        'posts': posts,
        'title': 'Posts'
    }
    return render(request, 'posts/index.html', context)
