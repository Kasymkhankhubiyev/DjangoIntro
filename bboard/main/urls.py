from django.urls import path
from .views import index, other_page, BBLoginView, profile, BBLogoutView, ChangeUserInfoView
from .views import BBpasswordChangeView

## создаем список маршрутов на уровне приложения

app_name = 'main'
urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBpasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),  ## задали псевдоним
]