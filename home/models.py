from django.db import models
from django.contrib.auth.models import User
import datetime

class Base (models.Model):
    created_at = models.DateTimeField(default=datetime.date.today)
    updated_at = models.DateTimeField(default=datetime.date.today)
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        abstract = True

class Writer (Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return user.name

class Article (Base):
    writer_id = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=datetime.date.today)
    def __str__(self):
        return self.title

class Element (Base):
    Article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class MidiaVisual (Element):
    src = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'image/', null=True)
    alt = models.CharField(max_length=200)
    width = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    srs_link = models.IntegerField(max_length=200)
    def __str__(self):
        return self.alt

class Paragraph (Element):
    text = models.CharField(max_length=5000)
    Article_ID = models.IntegerField(default = 0)

class YouTube (Element):
    src = models.CharField(max_length=200)