from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("""<html><head><meta name="google-site-verification" content="xA--Rda1Wb4WwB6GcwF3dYI7K3dPDTQTD2oZSWmSxdw" /><title>Myyttinen rationaalisuus</title></head><body><h1>Myyttinen rationaalisuus</h1><p>Tulossa pian!</p></body></html>""")
