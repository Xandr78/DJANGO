from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name, self.price, self.image, self.release_date, self.lte_exists, self.slug