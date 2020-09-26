from django.contrib import admin

from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'text', 'rating')
    list_filter = ('rating',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)