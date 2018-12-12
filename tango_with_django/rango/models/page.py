from django.db import models
from .category import Category

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 50)
    views = models.IntegerField(default = 0)
    url = models.URLField(max_length = 200)

    def __unicode__(self):
        return self.title
