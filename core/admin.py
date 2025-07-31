from django.contrib import admin

from core.models import Clothes, Post, RentalRequest, Transaction

admin.site.register(Clothes)
admin.site.register(Post)
admin.site.register(RentalRequest)
admin.site.register(Transaction)
