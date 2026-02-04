
from django.shortcuts import render


def blog(request):
    print('blog')
    return render(
        request,
        'blog/blog.html'
    )


def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )