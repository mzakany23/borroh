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
	url(r'^account/profile/address/add/(?P<id>\d+)/$','add_address',name='add_address'),
	url(r'^account/profile/address/show/$','show_address',name='show_address'),
	url(r'^account/profile/auth/edit/$','edit_auth',name='edit_auth'),
	url(r'^account/profile/info/$','profile_info',name='profile_info'),
	url(r'^account/profile/wishlist/$','user_wishlist',name='user_wishlist'),
	url(r'^account/profile/wishlist/add/(?P<id>\d+)$','add_to_wishlist',name='add_to_wishlist'),
	url(r'^account/profile/wishlist/delete/(?P<id>\d+)$','delete_from_wishlist',name='delete_from_wishlist'),
)

# products
urlpatterns += patterns('product.views',
	url(r'^products/details/(?P<id>\d+)$','product_detail',name='product_detail'),
	url(r'^products/detail/(?P<id>\d+)$','product_detail_non_json',name='product_detail_non_json'),
)

# media
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

# cart
urlpatterns += patterns('cart.views',
	url(r'^cart/show', 'cart_show',name='cart_show'),
	url(r'^cart/add/(?P<id>\d+)', 'add_item',name='add_item'),
	url(r'^cart/delete/(?P<id>\d+)', 'delete_item',name='delete_item'),	
)

# order 
urlpatterns += patterns('order.views',
	url(r'^order/start_order/', 'start_order_process',name='start_order_process'),	
	url(r'^order/auth/', 'order_auth',name='order_auth'),	
	url(r'^order/address/', 'order_address',name='order_address'),	
	url(r'^order/billing/', 'order_billing',name='order_billing'),	
	url(r'^order/shipping/', 'order_shipping',name='order_shipping'),	
	url(r'^order/payment/', 'order_payment',name='order_payment'),	
	url(r'^order/show/', 'order_show',name='order_show'),	
	
)










