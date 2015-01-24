from django.contrib import admin
from diogenes.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'year',
        'publisher',
        'ISBN',
        'genre',
    )

admin.site.register(Book, BookAdmin)
admin.site.site_header = 'Biblioteca de Diogenes'
