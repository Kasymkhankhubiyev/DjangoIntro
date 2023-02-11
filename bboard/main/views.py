from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


def other_page(request: HttpRequest, page) -> HttpResponse:
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


# Создаем контроллер для логирования в систему:
class BBLoginView(LoginView):
    template_name = 'main/login.html'


# создаем контроллер для вывода пользовательского профиля
@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/profile.html')


# создаем контроллер для выхода пользователя
class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name='main/logout.html'


# создаем контроллер на базе высокоуровневого класса для
# для правки данных пользователя
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

# Создаем контроллер для смены пароля пользователя,
# выводит соответствующую страницу
class BBpasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'

# Создадим контроллер-класс, регистрирующий пользователя
class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

# Создадим контроллер, который будет выводить сообщеня
# об успешной регистрации нового пользователя
class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'
