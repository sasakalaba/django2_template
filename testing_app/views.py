from django.http import HttpResponse
from django.template import loader
from testing_app.forms import CheckoutForm


def index(request):
    template = loader.get_template('index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def checkout(request):
    template = loader.get_template('checkout.html')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        # TODO: validation
        if form.is_valid():
            pass
        else:
            pass

    else:
        form = CheckoutForm()

    context = {'form': form}

    return HttpResponse(template.render(context, request))
