from django.contrib import admin

from models import Order

class OrderAdmin(admin.ModelAdmin):
	list_display = ['cart','user','type_of_cart']
	class Meta:
		model = Order

admin.site.register(Order,OrderAdmin)
