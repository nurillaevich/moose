from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_created=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name
