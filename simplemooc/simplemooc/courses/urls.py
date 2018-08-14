from django.urls import include, re_path
from simplemooc.courses import views as courses_views

urlpatterns = [
    re_path(r'^$', courses_views.index, name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/$', courses_views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/inscricao/$', courses_views.enrollment, name='enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', courses_views.undo_enrollment,
        name='undo_enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/$', courses_views.announcements,
        name='announcements'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', courses_views.show_announcement,
        name='show_announcement'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/$', courses_views.lessons, name='lessons'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', courses_views.lesson, name='lesson'),
    re_path(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', courses_views.material, name='material'),
              ]
