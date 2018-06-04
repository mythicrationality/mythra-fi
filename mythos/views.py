from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

# def index(request):
#     return HttpResponse("""<html><head><meta name="google-site-verification" content="xA--Rda1Wb4WwB6GcwF3dYI7K3dPDTQTD2oZSWmSxdw" /><title>Myyttinen rationaalisuus</title></head><body><h1>Myyttinen rationaalisuus</h1><p>Tulossa pian!</p></body></html>""")

def index(request):
    template = loader.get_template('mythos/index.html')
    return HttpResponse(template.render({}))


def contact(request):
    template = loader.get_template('mythos/contact.html')
    return HttpResponse(template.render({}))


def midsummer_redirect(request):
    return redirect("https://docs.google.com/document/d/1h_QssM0ZvnE7kqN1XFfN8VlR1Pms0PW8r9xbyWiKYJI/")
