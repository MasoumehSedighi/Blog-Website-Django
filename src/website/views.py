from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages

# Create your views here.


def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    """
    Handle the submission of the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request,'your message submited successfully')
        else:
            messages.error(request,'your message did not submited')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def elements_view(request):
    return render(request, 'website/elements.html')
