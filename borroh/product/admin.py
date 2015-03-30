from django.contrib import admin
from models import Product,Image,Variant,VariantSelection,Category

class ProductAdmin(admin.ModelAdmin):
	class Meta:
		model = Product

class ImageAdmin(admin.ModelAdmin):
	class Meta:
		model = Image

class VariantAdmin(admin.ModelAdmin):
	class Meta:
		model = Variant

class VariantSelectionAdmin(admin.ModelAdmin):
	class Meta:
		model = VariantSelection

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(Product,ProductAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Variant,VariantAdmin)
admin.site.register(VariantSelection,VariantSelectionAdmin)
admin.site.register(Category,CategoryAdmin)