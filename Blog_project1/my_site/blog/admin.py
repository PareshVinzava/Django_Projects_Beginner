from django.contrib import admin

from .models import post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug":("title",)}  # In prepopulated_fields always we have to give key value never foregt it.
    # This fields should bbe tuples that's why i've used here comma at end for making it tuple.

admin.site.register(post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
