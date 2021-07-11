from django.contrib import admin
#from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment  

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'thumbnail',
        'description',
        'short_descripton',
        'creation',


    ]
    #summernote_fields = ('description',)
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'body',
    ]

admin.site.register(Comment,CommentAdmin)
