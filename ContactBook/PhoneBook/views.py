from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

# Create your views here.

@login_required(login_url="/sign_in/")
def add_contact(request):
    form = ContactForm(data=request.POST or None)
    if form.is_valid() and request.method == "POST":
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Контакт успішно додано!")
        return redirect("get_contacts")
    
    return render(request=request, template_name="add_contact.html", context=dict(form=form))

@login_required(login_url="/sign_in/")
def get_contacts(request):
    contacts = Contact.objects.filter(user=request.user).all()
    return render(request=request, template_name="contacts.html", context=dict(contacts=contacts))

