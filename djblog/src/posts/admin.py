from django.contrib import admin

# Register your models here.
from .models import Post   

class PostAdmin (admin.ModelAdmin):
    list_display = ['title','active']
    search_fields = ['title']
    list_filter = ['active']
    
    

admin.site.register(Post,PostAdmin)