from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import re


class Book(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    clean_title = models.CharField(max_length=128, blank=True)
    author = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    publisher = models.CharField(max_length=128, blank=True)
    ISBN = models.CharField(max_length=128, blank=True)
    genre = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.author = self.first_name + ' ' + self.last_name
        self.slug = slugify(self.title)
        pattern = re.compile(r'(^the )|(^a )', re.IGNORECASE)
        result = pattern.search(self.title)
        if result:
            self.clean_title = pattern.sub("", self.title)
        else:
            self.clean_title = self.title

        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title