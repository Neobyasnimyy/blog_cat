from django.contrib import admin
from .models import Post
# Register your models here.

# Чтобы наша модель стала доступна на странице администрирования, нам нужно зарегистрировать её при помощи
admin.site.register(Post)