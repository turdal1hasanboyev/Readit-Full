from django.shortcuts import render

from .models import Client


def about(request):
    clients = Client.objects.filter(is_active=True).order_by('id')

    return render(request, 'about.html', {"clients": clients})
