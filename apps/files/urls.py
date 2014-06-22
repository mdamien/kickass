from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'files.views.file_list'),
    url(r'^upload/$', 'files.views.upload'),
    url(r'^details/(\d+)/$', 'files.views.details'),
    url(r'^admin/', include(admin.site.urls)),
]
