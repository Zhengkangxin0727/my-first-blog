from django.contrib import admin
from .models import Post
#.models代表同一个文件夹里models.py里的Post类
admin.site.register(Post)
#Post代表的是models里写的类
# Register your models here.
