from django.http import HttpRequest
from django.urls import reverse
from django.shortcuts import redirect


def redirect_to_swagger(request: HttpRequest):
    return redirect(reverse('swagger-doc'))