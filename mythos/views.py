from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

def index(request):
    template = loader.get_template('mythos/index.html')
    return HttpResponse(template.render({}))


def contact(request):
    template = loader.get_template('mythos/contact.html')
    return HttpResponse(template.render({}))


def introduction_kaj(request):
    template = loader.get_template('mythos/introduction/kaj.html')
    return HttpResponse(template.render({}))


def introduction_lumi(request):
    template = loader.get_template('mythos/introduction/lumi.html')
    return HttpResponse(template.render({}))


def midsummer_redirect(request):
    return redirect("https://docs.google.com/document/d/1h_QssM0ZvnE7kqN1XFfN8VlR1Pms0PW8r9xbyWiKYJI/")
