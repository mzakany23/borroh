from django.contrib import admin

from models import Cart,LineItem

class CartAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','total_price','total_points']
	class Meta:
		model = Cart

class LineItemAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','product','borroh']
	class Meta:
		model = LineItem

admin.site.register(Cart,CartAdmin)
admin.site.register(LineItem,LineItemAdmin)