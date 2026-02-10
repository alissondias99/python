
from django.shortcuts import render


def blog(request):
    print('blog')
    return render(
        request,
        'blog/blog.html',
        {
            'text': 'Estamos no blog' # ← context, define comportamentos da página
        }
    )


def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html',
        {
            'text': 'Estamos no exemplo' # ← context, define comportamentos da página
        }
    )