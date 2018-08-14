from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from simplemooc.core import urls as core_urls

admin.autodiscover()

"""urlpatterns = patterns('',
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^conta/', include('simplemooc.accounts.urls', namespace='accounts')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
)"""

urlpatterns = [
    re_path(r'^', include(('simplemooc.core.urls', 'core'),namespace='core')),
    re_path(r'^conta/', include(('simplemooc.accounts.urls', 'accounts'), namespace='accounts')),
    re_path(r'^cursos/', include(('simplemooc.courses.urls', 'courses'))),
    re_path(r'^admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )