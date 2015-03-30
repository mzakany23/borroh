from django.contrib import admin
from models import Product,Image,Category

class ProductAdmin(admin.ModelAdmin):
	fields = ['title','slug','description','price', 'image','points_price','borrohed','sold','discount','status','created','updated']
	readonly_fields = ('product_code','slug','created','updated')
	class Meta:
		model = Product

class ImageAdmin(admin.ModelAdmin):
	class Meta:
		model = Image

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(Product,ProductAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category,CategoryAdmin)

