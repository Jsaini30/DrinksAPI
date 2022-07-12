from csv import writer
from django.contrib import admin
from .models import Drink, book, Writer

admin.site.register(Drink)


class Drinksadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Writer)


class Writersadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']


admin.site.register(book)


class Booksadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'totalpages', 'category']
