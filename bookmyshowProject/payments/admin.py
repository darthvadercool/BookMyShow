from django.contrib import admin


from .models import Coupon, Payment


admin.site.register(Coupon)
admin.site.register(Payment)
