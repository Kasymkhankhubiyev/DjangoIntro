from django.urls import path
from .views import index

## создаем список маршрутов на уровне приложения

app_name = 'main'
urlpatterns = [
    path('', index, name='index')  ## задали псевдоним
]