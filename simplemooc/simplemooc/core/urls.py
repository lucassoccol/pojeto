from django.urls import include, re_path
from simplemooc.core import views as core_views

"""urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)"""

urlpatterns = [
    re_path(r'^$', core_views.home, name='home'),
    re_path(r'^contato/$', core_views.contact, name='contact'),
]










"""
from django.contrib.auth import views as auth_views
from myapp import views as myapp_views

urlpatterns = [
    url(r'^$', myapp_views.home, name='home'),
    url(r'^contact/$', myapp_views.contact, name='contact'),
    url(r'^login/$', auth_views.login, name='login'),
]"""