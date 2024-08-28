from django.contrib import admin

from .models import Category, Comment, Tag, Article


admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'author',
        'views',
        'created_at',
    )
    prepopulated_fields = {'slug': ('name',)}
