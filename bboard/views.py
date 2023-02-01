from django.http import HttpResponse
from django.http import HttpRequest

def index(request: HttpRequest):
    """
        request - хранит различную информацию о запросе:
        - запрашиваемый интернет-адрес
        - данные, полученные от посетителя
        - служебную информацию от веб-абозревателя и т.д.
    """
    return HttpResponse("Здесь будет выведен список объявлений")
