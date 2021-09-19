from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print('Message sent.')
            print(f'Name: {name}')
            print(f'Email: {email}')
            print(f'Subject: {subject}')
            print(f'Message: {message}')

            messages.success(request, 'Email delivered.')
            form = ContactForm()
        else:
            messages.error(request, ' Email failed to send')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)


def product(request):
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Name: {prod.name}')
            print(f'Price: {prod.price}')
            print(f'Storage: {prod.storage}')
            print(f'Image: {prod.image}')

            messages.success(request, 'Product successfuly saved')
            form = ProductModelForm()
        else:
            messages.error(request, 'Product failed to save')
    else:
        form = ProductModelForm()
    context = {
        'form': form
    }
    return render(request, 'product.html', context)
