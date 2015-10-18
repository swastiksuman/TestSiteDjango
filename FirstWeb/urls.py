from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/$', 'joins.views.home', name='home'),
    url(r'^home2/$', 'joins.views.home2', name='home2'),
    url(r'^admin/', include(admin.site.urls)),
)
