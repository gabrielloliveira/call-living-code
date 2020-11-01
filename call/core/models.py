from django.db import models


class Person(models.Model):
    name = models.CharField('nome', max_length=500)

    def __str__(self):
        return self.name
