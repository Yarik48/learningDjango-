from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Posts(models.Model):
    text = models.CharField(max_length=100)
    day = models.ForeignKey('Day', on_delete=models.CASCADE)
    date = models.DateField(null=True)
    object = models.ForeignKey('Object', on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True, upload_to='files/')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class Day(models.Model):
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('day', kwargs={'pk': self.pk})


class Object(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('obj', kwargs={'pk': self.pk})


class Messages(models.Model):
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.pk}, {self.text}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


