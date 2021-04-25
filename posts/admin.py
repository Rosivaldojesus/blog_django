from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titulo_post', 'autor_post', 'data_post', 'categoria_post', 'publicado_post')

admin.site.register(Post, PostAdmin)