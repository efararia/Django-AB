from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from website.forms import ContactForm, NewsLetterForm
from django.contrib import messages

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticked submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticked didnt submitted successfully')  
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
