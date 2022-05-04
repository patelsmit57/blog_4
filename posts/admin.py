from django.contrib import admin
from .models import Author,BlogModel, CommentModel

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(BlogModel, BlogAdmin)
admin.site.register(Author)
admin.site.register(CommentModel)
