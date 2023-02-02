from django.http import HttpResponse
from django.http import HttpRequest
# from django.template import loader
from django.shortcuts import render

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
    # template = loader.get_template('bboard/index.html')  # Возвращает экземпляр класса Template
    bbs = Bb.objects.all()  # .order_by('-published')  # Формируем контекст/содержимое шаблона - набор данных для вывода
    context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))  # рендерим содержимое веб страницы
    return render(request=request, template_name='bboard/index.html', context=context)
