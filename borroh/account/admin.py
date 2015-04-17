from django.contrib import admin
from models import Profile, Address

class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile


class AddressAdmin(admin.ModelAdmin):
	class Meta:
		model = Address

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Address,AddressAdmin)