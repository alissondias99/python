from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact

def index(request):

    # somente contatos com show = True iram aparecer na página
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id') 
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'contact/index.html',
        {
            'page_obj': page_obj,
            'title': 'Contatos -',
        }
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '': # barra de pesquisa vazia = redireciona para a base
        return redirect('contact:index')
    
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
                Q(first_name__icontains = search_value,) |
                Q(last_name__icontains = search_value,) |
                Q(phone__icontains = search_value,) |
                Q(email__icontains = search_value,)
                ) \
        .order_by('-id') 

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'contact/index.html',
        {
            'page_obj': page_obj,
            'title': 'Search -',
        }
    )

def contact(request, contact_id): # essa view será usada quando um contato específico for procurado

    single_contact = get_object_or_404( 
        Contact, pk = contact_id, show=True
    )

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    return render(
        request,
        'contact/contact.html',
        {
            'contact': single_contact,
            'title': site_title,
        }
    )