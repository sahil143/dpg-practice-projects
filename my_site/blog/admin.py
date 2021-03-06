from django.contrib import admin

# Register your models here.

from .models import Comment, Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "date",)
  list_filter = ("author", "tags", "date",)
  prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
  list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

