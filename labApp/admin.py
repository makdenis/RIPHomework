from django.contrib import admin
from .models import *

# # Register your models here.
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     #fields = ('first_name', 'last_name')
#     list_display = ('username','full_name','count_of_orders',)
#     list_filter = ('first_name',)
#     search_fields = ['last_name', 'first_name']
#
#     def full_name(self, obj):
#         return "{} {}".format(obj.last_name, obj.first_name)
#
#     def username(self, obj):
#         return "{}".format(obj.user.username)
#
#     def count_of_orders(self, obj):
#         ord = Usluga.objects.filter(user=obj)
#         return len(ord)
#
#
# @admin.register(zakaz)
# class ProdactAdmin(admin.ModelAdmin):
#     empty_value_display = '-empty-'
#     # list_display = ('prodact','price','description',)
#     # list_filter = ('price',)
#     # search_fields = ['name']
#     #
#     # def prodact(self, obj):
#     #     return "{}".format(obj.prodact_name)
#     #
#     # def price(self, obj):
#     #     return "{}".format(obj.price)
#     #
#     # def description(self, obj):
#     #     return "{}".format(obj.description)
#
#
#
#
# @admin.register(Usluga)
# class OrderAdmin(admin.ModelAdmin):
#     empty_value_display = '-empty-'
#     # fields = ('username', 'prodact', 'date')
#     # list_display = ('username', 'prodact', 'date')
#     # list_filter = ('user_zakaz',)
#     # search_fields = ['user_zakaz']
#     #
#     # def username(self, obj):
#     #     return "{}".format(obj.user.user)
#     #
#     # def prodact(self, obj):
#     #     return obj.prodact.prodact_name
#     #
#     # def date(self, obj):
#     #     return "{}".format(obj.order_date)
