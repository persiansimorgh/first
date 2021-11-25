from django.contrib import admin
from .models import Post
from .models import Videos

admin.site.register(Videos)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass



