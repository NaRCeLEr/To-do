from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1250, null=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Tasks", kwargs={"slug": self.slug})


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1250, null=True)
    days_number = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/task/{self.slug}/'




