from django.contrib import admin
from blog.models import Post, Catagory


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Catagory, CategoryAdmin)
