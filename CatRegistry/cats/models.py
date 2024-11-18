from django.db import models

class Cat(models.Model):
    SEXUALITY_CHOICES = [
        ('M', 'Male ♂️'),
        ('F', 'Female ♀️'),
    ]
    COLOR_CHOICES = [
        ('white', 'White 🐾'),
        ('black', 'Black 🐾'),
        ('orange', 'Orange 🐾'),
        ('gray', 'Gray 🐾'),
        ('calico', 'Calico 🐾'),
    ]

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sexuality = models.CharField(max_length=1, choices=SEXUALITY_CHOICES, default='M')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='white')

    def __str__(self):
        return self.name
