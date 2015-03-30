from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
 		url(r'^$', 'home.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('product.views',
	# url(r'^products/list$','product_list',name='product_list'),
)

# media
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

