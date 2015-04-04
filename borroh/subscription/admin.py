from django.contrib import admin

from models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
	class Meta:
		model = Subscription

admin.site.register(Subscription,SubscriptionAdmin)
