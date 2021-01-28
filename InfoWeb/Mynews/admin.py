from django.contrib import admin
from Mynews.models import Post

# Register your models here.
class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'writer', 'article', 'href')
    list_filter = ('title',)
    search_fields = ('title', 'writer','article')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, WebAdmin)
