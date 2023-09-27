from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    name = 'Nurdaulet'

    context = {
        'name': name,
    }

    return render(request=request, template_name='app/index.html', context=context)


