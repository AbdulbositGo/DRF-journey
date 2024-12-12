from django.contrib import admin

from .models import User, Product, Order, OrderItem


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = (
        "order",
        "product",
        "quantity",
    )
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    fields = (
        "order_id",
        "user",
        "created",
        "status",
    )
    readonly_fields = ['created']
    inlines = [OrderItemTabularInline]


admin.site.register([User, Product])
