from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts

def blog(request):
   
    context = { # ← define comportamentos da página
        'text': 'Olá blog',
        'posts': posts
    }
    
    return render(
        request,
        'blog/blog.html',
        context 
        
    )

def post(request, post_id):

    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não existe')

    context = {
        'post': found_post # somente o post selecionado será exibido
    }
    
    return render(
        request,
        'blog/post.html',
        context 
        
    )

def exemplo(request):
    
    return render(
        request,
        'blog/exemplo.html',
        {
            'text': 'Estamos no exemplo' 
        }
    )