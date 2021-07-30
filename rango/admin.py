from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile



class Pageadmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, Pageadmin)
admin.site.register(UserProfile)

# Register your models here.
