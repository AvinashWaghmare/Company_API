from django.contrib import admin
from api.models import User, Post

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body','author')


admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)