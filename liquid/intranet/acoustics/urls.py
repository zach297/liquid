from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'intranet.acoustics.views.main'),
    url(r'^skip$', 'intranet.acoustics.views.skip'),
    url(r'^state$', 'intranet.acoustics.views.state'),
    url(r'^search$', 'intranet.acoustics.views.search'),
    url(r'^queue$', 'intranet.acoustics.views.queue'),
    url(r'^vote$', 'intranet.acoustics.views.vote'),
)
