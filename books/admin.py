from django.contrib import admin

from .models import Author, Category, Book
from import_export import resources
from import_export.admin import ExportActionMixin, ExportMixin


class AuthorAdmin(ExportActionMixin, admin.ModelAdmin):
    search_fields = ['name']


class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    search_fields = ['name']


class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['published']
    search_fields = ['name']


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
