from django.contrib import admin
from models import Profile, Address, EmailReset, UserCreditCard

class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile


class AddressAdmin(admin.ModelAdmin):
	class Meta:
		model = Address

class EmailResetAdmin(admin.ModelAdmin):
	class Meta:
		model = EmailReset

class UserCreditCardAdmin(admin.ModelAdmin):
	class Meta:
		model = UserCreditCard

admin.site.register(EmailReset,EmailResetAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(UserCreditCard,UserCreditCardAdmin)
