from django.contrib import admin
from Models.models import User, Product, Order, Profile, Contact, Category, Cart, \
    Review, OrderItem, ShippingAddress, Payment, Coupon, Refund

# Register your models here.


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)

