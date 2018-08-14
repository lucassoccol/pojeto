from django.urls import include, re_path
from simplemooc.accounts import views as accounts_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    re_path(r'^$', accounts_views.dashboard, name='dashboard'),
    re_path(r'^entrar/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    re_path(r'^sair/$', auth_views.logout, {'next_page': 'core:home'}, name='logout'),
    re_path(r'^cadastre-se/$', accounts_views.register, name='register'),
    re_path(r'^nova-senha/$', accounts_views.password_reset, name='password_reset'),
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$', accounts_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^editar/$', accounts_views.edit, name='edit'),
    re_path(r'^editar-senha/$', accounts_views.edit_password, name='edit_password'),
]