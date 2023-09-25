from django.contrib import admin
from newspaper.models import Post, Tag, Category, Contact
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)