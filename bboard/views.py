from django.http import HttpResponse
from django.http import HttpRequest

from .models import Bb

def index(request: HttpRequest) -> HttpResponse:
    """
        request - хранит различную информацию о запросе:
        - запрашиваемый интернет-адрес
        - данные, полученные от посетителя
        - служебную информацию от веб-абозревателя и т.д.


        ********
        Данная функция выводит все записи в порядке убывания даты публикации
        на это указывает знак минус перет атрибутом функции - название колонки со знаком минус

    """

    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
