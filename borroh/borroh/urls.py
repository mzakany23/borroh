from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# home
urlpatterns = patterns('',
 		url(r'^$', 'home.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

# account
urlpatterns += patterns('account.views',
	url(r'^account/login$','auth_login',name='auth_login'),
	url(r'^account/logout$','auth_logout',name='auth_logout'),
	url(r'^account/create$','auth_create_account',name='auth_create_account'),
	url(r'^account/profile/(?P<id>\d+)/$','user_profile',name='user_profile'),
)

# products
urlpatterns += patterns('product.views',
	# url(r'^products/list$','product_list',name='product_list'),
)

# media
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

