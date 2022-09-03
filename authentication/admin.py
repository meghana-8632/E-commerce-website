from django.contrib import admin
from authentication.models import Item,Customer
class AdminItem(admin.ModelAdmin):
    list_display=['name','price']
admin.site.register(Item,AdminItem)
admin.site.register(Customer)














