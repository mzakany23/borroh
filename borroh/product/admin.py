from django.contrib import admin
from models import Product,Image,Category,Collection,Brand

class ProductImageInline(admin.TabularInline):
	model = Image

class ProductAdmin(admin.ModelAdmin):
	fields = ['title','slug','description','category','brand','featured','gender','price','points_price','borrohed','sold','discount','status','size','created','updated']
	readonly_fields = ('product_code','slug','created','updated')
	inlines = [ProductImageInline]
	class Meta:
		model = Product

class ImageAdmin(admin.ModelAdmin):
	class Meta:
		model = Image

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','gender']
	ordering = ['-gender']
	class Meta:
		model = Category

class CollectionAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','name']
	class Meta:
		model = Collection

class BrandAdmin(admin.ModelAdmin):
	class Meta:
		model = Brand

admin.site.register(Product,ProductAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(Brand,BrandAdmin)