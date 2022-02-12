from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
posts = [
    {
        'author': 'Peter',
        'title': 'Blog Post 1',
        'content': 'Content of First post',
        'date_created': "Feb 3, 2022"
    },
    {
            'author': 'parker',
            'title': 'Blog Post 2',
            'content': 'Content of second post',
            'date_created': "Feb 1, 2022"
        }
]

def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()

    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
