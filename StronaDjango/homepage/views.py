from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'Homepage/index.html', {})
    # return HttpResponse("Hello, world. You're at the products index.")


# Create your views here.
