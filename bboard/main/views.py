from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


def other_page(request: HttpRequest, page) -> HttpResponse:
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
