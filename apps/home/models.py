from django.db import models


class Checkmarks(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Checkmark'
        verbose_name_plural = 'Checkmarks'

    def __str__(self):
        return self.name
