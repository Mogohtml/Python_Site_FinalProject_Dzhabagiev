from django.contrib import admin

from core.models import Size, Clothes, Post, RentalRequest, Transaction, Category

# Register your models here.
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Clothes)
admin.site.register(Post)
admin.site.register(RentalRequest)
admin.site.register(Transaction)
