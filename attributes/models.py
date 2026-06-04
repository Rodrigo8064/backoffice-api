from django.db import models

from category.models import Family


class Attribute(models.Model):
    name = models.CharField(max_length=150)
    expected_value = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    families = models.ManyToManyField(
        Family,
        related_name='attributes',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Attribute'
        ordering = ['name']
