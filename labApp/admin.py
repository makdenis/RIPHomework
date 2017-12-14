from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',
    'customer_name',
    'email',
    'first_name',
    'last_name'
    )
    # fields = ('first_name', 'last_name')
    # list_display = ('username','full_name','count_of_orders',)
    # list_filter = ('first_name',)
    # search_fields = ['last_name', 'first_name']
    #
    # def full_name(self, obj):
    #     return "{} {}".format(obj.last_name, obj.first_name)
    #
    # def username(self, obj):
    #     return "{}".format(obj.user.username)


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
class BelongTOInline(admin.TabularInline):
    model = BelongTO
    extra = 1
    verbose_name_plural = 'Orders list'
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def total(self, request):
        total = 0
        items = BelongTO.objects.filter(order_id=request.code)
        for i in items:
            computer = Computer.objects.get(name=i.item_id)
            total += computer.price
        return total
    readonly_fields = ('total',)
    list_display = ('code', 'customer', 'total', 'is_open', 'date',)
    inlines = (BelongTOInline,)



@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    def orders(self, request):
        orders = []
        for s in BelongTO.objects.filter(item_id=request.name):
            orders.append(s.order_id)
        return orders
    inlines = (BelongTOInline,)
    list_display = ('name',
                    'price',
                    'description',
                    'pic',
                    'type',
                    'quantity',
                    'orders')