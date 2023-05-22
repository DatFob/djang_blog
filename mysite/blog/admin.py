from django.contrib import admin
from .models import Post

@admin.register(Post)   # decorator
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','published','status']
# Register your models here