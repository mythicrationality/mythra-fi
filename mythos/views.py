from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'mythos/index.html')


def contact(request):
    return render(request, 'mythos/contact.html')


def introduction_index(request):
    return render(request, 'mythos/introduction/index.html')


def introduction_king_may(request):
    return render(request, 'mythos/introduction/king_may.html')


def introduction_lumi(request):
    return render(request, 'mythos/introduction/lumi.html')


def introduction_tiina(request):
    return render(request, 'mythos/introduction/tiina.html')


def material_index(request):
    return render(request, 'mythos/material_wip.html')


def midsummer_redirect(request):
    return redirect("https://docs.google.com/document/d/1h_QssM0ZvnE7kqN1XFfN8VlR1Pms0PW8r9xbyWiKYJI/")
