from django.contrib import admin

from models import Shipping

class ShippingAdmin(admin.ModelAdmin):
	class meta:
		model = Shipping

admin.site.register(Shipping,ShippingAdmin)
