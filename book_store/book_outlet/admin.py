from django.contrib import admin

from .models import BOOK,Author,Address,Country

# Register your models here.

# In admin panel if add new entry then it will show some field which have to fill but suppose we have fiels named slug and if i dont fill it admin panel will not allow me to add new data. and we already have overwitten thr save() method which automatically add slugs (-) to title,
# so Now solution is we can change in admin panel to what to ask when do anew data entry. 


class BOOKAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")

admin.site.register(BOOK,BOOKAdmin) # first agrument is name of model which we have register and second is not compulsoury if i have created class for advance admin panel changes then i have to mention that class name to here as second argument.
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)