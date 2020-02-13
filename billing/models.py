from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


User = settings.AUTH_USER_MODEL


# Create your models here.
class Billing(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        Billing.objects.get_or_create(user=instance, email=instance.email)


post_save.connect(user_created_reciever, sender=User)
