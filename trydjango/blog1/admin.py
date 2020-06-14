from django.contrib import admin
from .models import post
class postAdmin(admin.ModelAdmin):
    list_display = ('title','updated','timestamp')
    list_display_links = ["updated"]
    list_filter = ('updated','timestamp')
    search_fields=('title','content')
    list_editable = ['title']
    class Meta:
        model=post
    '''prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']'''
admin.site.register(post,postAdmin)
