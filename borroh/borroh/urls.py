from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# home
urlpatterns = patterns('',
 		url(r'^$', 'home.views.home',name='home'),
 		url(r'^/error', 'home.views.error',name='error'),
    url(r'^admin/', include(admin.site.urls)),
)

# account
urlpatterns += patterns('account.views',
	# login/logout
	url(r'^account/login$','auth_login',name='auth_login'),
	url(r'^account/logout$','auth_logout',name='auth_logout'),
	url(r'^account/create$','auth_create_account',name='auth_create_account'),

	# user_profile
	url(r'^account/profile/$','user_profile',name='user_profile'),
	url(r'^account/profile/borroh/show/','show_borrohed',name='show_borrohed'),
	url(r'^account/profile/auth/edit/$','edit_auth',name='edit_auth'),
	
	# address
	url(r'^account/profile/address/add/','add_address',name='add_address'),
	url(r'^account/profile/address/show/$','show_address',name='show_address'),
	url(r'^account/profile/address/edit/(?P<id>\d+)/$','edit_address',name='edit_address'),
	url(r'^account/profile/address/delete/(?P<id>\d+)/$','delete_address',name='delete_address'),

	# orders
	url(r'^account/order/list/','account_order_list',name='account_order_list'),
	
	# password reset
	url(r'^account/profile/password_reset/$','user_password_reset',name='user_password_reset'),
	

	# credit cards
	url(r'^account/profile/credit-card/add/','add_card_to_stripe',name='add_card_to_stripe'),
	url(r'^account/profile/credit-card/delete/','delete_stripe_card',name='delete_stripe_card'),

	# user_info
	url(r'^account/profile/info/$','profile_info',name='profile_info'),
	url(r'^account/profile/info/edit$','profile_info_edit',name='profile_info_edit'),

	# wishlist
	url(r'^account/profile/wishlist/$','user_wishlist',name='user_wishlist'),
	url(r'^account/profile/wishlist/add/(?P<id>\d+)$','add_to_wishlist',name='add_to_wishlist'),
	url(r'^account/profile/wishlist/delete/(?P<id>\d+)$','delete_from_wishlist',name='delete_from_wishlist'),
	
	url(r'^account/login_as_guest/', 'login_as_guest',name='login_as_guest'),
	

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
	url(r'^cart/show/$', 'cart_show',name='cart_show'),
	url(r'^cart/show/buy', 'cart_show_buy',name='cart_show_buy'),
	url(r'^cart/show/borroh', 'cart_show_borroh',name='cart_show_borroh'),
	url(r'^cart/add/(?P<id>\d+)', 'add_item',name='add_item'),
	url(r'^cart/delete/(?P<id>\d+)', 'delete_item',name='delete_item'),	
)

# order 
urlpatterns += patterns('order.views',
	# validation
	url(r'^order/start_order/', 'start_order_process',name='start_order_process'),	
	url(r'^order/too-many-items-in-cart/', 'too_many_items_in_borroh_cart',name='too_many_items_in_borroh_cart'),
	url(r'^order/add-to-wishlist-and-remove/(?P<id>\d+)', 'add_to_wishlist_and_remove_from_cart',name='add_to_wishlist_and_remove_from_cart'),	
	url(r'^order/remove-from-cart-and-redirect-back/(?P<id>\d+)', 'remove_from_cart_and_back_to_borroh',name='remove_from_cart_and_back_to_borroh'),	
	
	# order process
	url(r'^order/auth/', 'order_auth',name='order_auth'),	
	url(r'^order/address/', 'order_address',name='order_address'),	
	url(r'^order/billing/', 'order_billing',name='order_billing'),	
	url(r'^order/shipping/', 'order_shipping',name='order_shipping'),	
	url(r'^order/payment/', 'order_payment',name='order_payment'),	
	url(r'^order/show/', 'order_show',name='order_show'),	
	url(r'^order/submit/', 'order_submit',name='order_submit'),	
	
)

urlpatterns += patterns('subscription.views',
	url(r'^subscription/subscribe/$','subscribe',name='subscribe'),
	url(r'^subscription/subscribe/thanks','subscription_thank_you',name='subscription_thank_you'),
)








