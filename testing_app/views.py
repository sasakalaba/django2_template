from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def checkout(request):
    template = loader.get_template('checkout.html')
    context = {}

    return HttpResponse(template.render(context, request))
