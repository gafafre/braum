from django.db import models
from core.models import Base
from writers.models import Writer
from django.utils.text import slugify


class Article (Base):
    writer_id = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    publish_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Element (Base):
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)
    order = models.FloatField()

    class Meta:
        abstract = True


class MidiaVisual (Element):
    src = models.CharField(max_length=200)
    alt = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    src_link = models.CharField(max_length=200)

    def __str__(self):
        return self.alt


class Paragraph (Element):
    text = models.TextField()


class YouTube (Element):
    src = models.CharField(max_length=200)
    autoplay = models.BooleanField(default=False)
    loop = models.BooleanField(default=False)
    start = models.IntegerField(blank=True, null=True)
