from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    search_fields = ['title', 'body']

admin.site.register(Post, PostAdmin)
