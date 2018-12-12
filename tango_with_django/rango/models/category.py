from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length = 130, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    comments = models.CharField(max_length = 600, default='')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
