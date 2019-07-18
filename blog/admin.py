from django.contrib import admin

from .models import Post, Comment    #import class Post from models.py

admin.site.register(Post)   #register class Post --> Blog.Post shows up in 'admin/' page
admin.site.register(Comment)