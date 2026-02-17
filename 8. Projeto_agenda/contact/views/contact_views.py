from django.shortcuts import render, get_object_or_404
from contact.models import Contact

def index(request):

    # somente contatos com show marcado iram aparecer na página
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id') 

    return render(
        request,
        'contact/index.html',
        {
            'contacts': contacts,
            'title': 'Contatos -',
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