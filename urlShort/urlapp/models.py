from django.db import models
from django.contrib.auth.hashers import make_password


class UrlData(models.Model):
    url = models.CharField(max_length=400, null=True)
    file = models.CharField(null=True, max_length=200)
    slug = models.CharField(max_length=15)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Short Url is : {self.slug}"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UrlData, self).save(*args, **kwargs)
