from django.urls import path 
from . import views

urlpatterns = [
    path('add_product', views.add_product, name='add_product'),
    path('edit_product', views.edit_product, name='edit_product'),
    path('delete_product', views.delete_product, name='delete_product'),
    path('add_review', views.add_review, name='add_review'),
    path('delete_review', views.delete_review, name='delete_review'),
    path('add_cart', views.add_cart, name='add_cart'),
    path('delete_cart', views.delete_cart, name='delete_cart'),
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist', views.delete_wishlist, name='delete_wishlist'),
    path('add_payment', views.add_payment, name='add_payment'),
    path('delete_payment', views.delete_payment, name='delete_payment'),
    path('add_order', views.add_order, name='add_order'),
    path('delete_order', views.delete_order, name='delete_order'),
    path('add_shipping_address', views.add_shipping_address, name='add_shipping_address'),
    path('delete_shipping_address', views.delete_shipping_address, name='delete_shipping_address'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('delete_contact', views.delete_contact, name='delete_contact'),
    path('add_category', views.add_category, name='add_category'),
    path('delete_category', views.delete_category, name='delete_category'),
    path('add_coupon', views.add_coupon, name='add_coupon'),
    path('delete_coupon', views.delete_coupon, name='delete_coupon'),
    path('edit_coupon', views.edit_coupon, name='edit_coupon'),
    path('add_refund', views.add_refund, name='add_refund'),
    path('delete_refund', views.delete_refund, name='delete_refund'),
    path('add_order_item', views.add_order_item, name='add_order_item'),
    path('delete_order_item', views.delete_order_item, name='delete_order_item'),
    
    
]