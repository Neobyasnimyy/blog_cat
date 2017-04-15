from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    # models.Model означает, что объект Post является моделью Django,
    # так Django поймет, что он должен сохранить его в базу данных.
    #author = models.ForeignKey('auth.User')  # ссылка на другую модель.
    title = models.CharField(max_length=200, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')  # upload_to=куда загружать
    #text = models.TextField(blank=True, null=True, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title