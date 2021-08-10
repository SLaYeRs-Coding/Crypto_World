from .models import News
from django.contrib import admin


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    '''Admin View for News'''

    list_display = ('title','text','category','date')
    list_filter = ('category','date')
    search_fields = ('title','text')
    ordering = ('title',)