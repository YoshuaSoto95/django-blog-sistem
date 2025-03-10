from django.contrib import admin
from .models import Category, Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude = ('create_at',)
    list_display = ('title', 'subtitle', 'image_main', 'content', 'categories', 'tags', 'create_at')

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('create_at',)
    list_display = ('name', 'create_at')

class TagAdmin(admin.ModelAdmin):
    exclude = ('create_at',)
    list_display = ('name', 'create_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
