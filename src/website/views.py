from django.shortcuts import render, redirect
from .forms import ContactForm

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
        print(form)
        if form.is_valid():
            form.save()
            return redirect('website:contact')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html')


def elements_view(request):
    return render(request, 'website/elements.html')
