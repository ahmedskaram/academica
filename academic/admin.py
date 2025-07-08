from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'term', 'is_available')
    list_filter = ('year', 'term', 'is_available')
    search_fields = ('title',)
    ordering = ('year', 'term')

admin.site.register(Book, BookAdmin)
