from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Book(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    year = models.IntegerField(blank=True)
    publisher = models.CharField(max_length=128)
    ISBN = models.CharField(max_length=128, blank=True)
    genre = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.author = self.first_name + ' ' + self.last_name
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

#User.book = property(lambda u: Book.objects.get(user=u))