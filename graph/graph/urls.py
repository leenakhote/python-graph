from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from graph_data import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^graph/$', views.query_with_fetchone),
    url(r'^graph/(?P<month>[0-9]+)$(?P<year>\w+)$', views.query_with_fetchone),
    url(r'^stats/$', views.statistics),
    url(r'^stats/submit/(?P<choice>[0-9]+)$', views.submit, name='submit'),
    url(r'^admin/', include(admin.site.urls)),

)
