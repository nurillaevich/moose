from django.contrib import admin
from .models import Article, Author, Comment, About, Tage, Contact


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ['id', 'name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ['id']
    # filter_horizontal = ['tag']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, BlogAdmin)
admin.site.register(Comment)
admin.site.register(About)
admin.site.register(Tage)
