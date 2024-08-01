from django.contrib import admin

from orders.models import Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    rew_id_fields = ['product']



class OrderAdmin(admin.ModelAdmin):
    list_filter = ['created','paid']
    inlines = [OrderItemInline]


admin.site.register(Order,OrderAdmin)
