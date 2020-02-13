from django.db import models
from product.models import product
from django.db.models.signals import pre_save, post_save
from ecommerece.utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    product = models.ManyToManyField(product, blank=True)

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
