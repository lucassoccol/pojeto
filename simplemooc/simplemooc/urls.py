from django.urls import include, path
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
    path(r'^', include(('simplemooc.core.urls', 'core'),namespace='core')),
    path(r'^conta/', include(('simplemooc.accounts.urls', 'accounts'), namespace='accounts')),
    path(r'^cursos/', include(('simplemooc.courses.urls', 'courses'), name='courses')),
    path(r'^admin/', 'admin.site.urls', name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )