from django.conf.urls import patterns, include, url

urlpatterns = patterns('djstaticfile.core.views',
    url(r'^$', 'home', name='home'),
)

