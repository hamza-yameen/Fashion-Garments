from django.shortcuts import render, HttpResponseRedirect
from .form import ContactForm
from django.contrib.auth import authenticate, login, get_user_model


def home(request):
    print(request.session.get('first_name'))
    context = {
        "title": "Home Page",
        "content": "Welcome to Home_Page"
    }
    return render(request, "home.html", context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contect Page",
        "content": "Welcome to Contect_Page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #   print(request.POST.get('fullname'))
    #  print(request.POST.get('email'))
    # print(request.POST.get('content'))

    return render(request, "contact/view.html", context)


def about(request):
    context = {
        "title": "About Page",
        "content": "Welcome to About_Page"
    }
    return render(request, "home.html", context)