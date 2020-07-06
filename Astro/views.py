from django.contrib import admin
from django.shortcuts import render, redirect
from .forms import ModalEnquiry, ModalOrder, ModalPrescription, PulllEnquiry
from .models import Enquiry, Prescription, Order
from django.contrib import messages


def panel(request):
    return redirect(admin.sites.urls)


def home(request):
    context = {
        "form": ModalPrescription
    }
    return render(request, 'home.html', context)


def products(request):
    return render(request, 'products.html')


def order(request):
    context = {
        "form": ModalOrder
    }
    return render(request, 'order.html', context)


def pull(request):
    context = {
        "form": PulllEnquiry

    }
    return render(request, 'enquiries.html', context)


def fetchEnquiry(request):
    form = PulllEnquiry(request.POST)
    enquiries = {'None': None}
    if form.is_valid():
        print('\n\n\n\n\n', form, '\n\n\n\n\n')
        print(form.cleaned_data['number'])
        enquiries = Enquiry.objects.filter(number=form.cleaned_data['number'])
    context = {
        'enquiries': enquiries
    }
    return render(request, 'results.html', context)


def contact(request):
    context = {
        "form": ModalEnquiry
    }
    return render(request, 'contact.html', context)


def addQuery(request):
    goto = 'home'
    form = ModalEnquiry(request.POST)

    if form.is_valid():
        form.save(Enquiry)
        messages.add_message(request, messages.SUCCESS, "Your enquiry has been submitted")
    else:
        goto = 'contact'
        messages.add_message(request, messages.WARNING, "This is an alphanumeric field, please use alphanumeric "
                                                        "characters  ONLY i.e. [0-9, a-z, A-Z]")

    return redirect(goto)


def addOrder(request):
    goto = 'home'
    form = ModalOrder(request.POST)
    if form.is_valid():
        form.save(Order)
        messages.add_message(request, messages.SUCCESS, "Your order has been submitted")
    else:
        goto = 'order'
        messages.add_message(request, messages.WARNING, "Your order has not been submitted")

    return redirect(goto)


def addPrescription(request):
    form = ModalPrescription(request.POST)

    if form.is_valid():
        form.save(Prescription)
        messages.add_message(request, messages.SUCCESS, "Your prescription request has been submitted")

    return redirect('home')

# Create your views here.
