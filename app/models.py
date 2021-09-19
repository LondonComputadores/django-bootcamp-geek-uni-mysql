from django.db import models

# Signals to pre save the slug instance of the class
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    created_at = models.DateField('Date of creation', auto_now_add=True)
    modified_at = models.DateField('Date of update', auto_now=True)
    active = models.BooleanField('Active', default=True)


class Product(Base):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    storage = models.IntegerField('Storage')
    image = models.ImageField('Image', upload_to='products')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(product_pre_save, sender=Product)
    
    
