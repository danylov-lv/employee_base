from django.db import models
import mptt
from django.utils import timezone

choices = (
    ('ceo', 'CEO'),
    ('deputy_ceo', 'Deputy CEO'),
    ('regional_manager', 'Regional Manager'),
    ('territorial_manager', 'Territorial Manager'),
    ('deputy_territorial_manager', 'Deputy Territorial Manager'),
    ('head_of_network', 'Head of Network'),
    ('pharmacist', 'Pharmacist')
)

posts = {
    'ceo': 'CEO',
    'deputy_ceo': 'Deputy CEO',
    'regional_manager': 'Regional Manager',
    'territorial_manager': 'Territorial Manager',
    'deputy_territorial_manager': 'Deputy Territorial Manager',
    'head_of_network': 'Head of Network',
    'pharmacist': 'Pharmacist'
}


class Employee(models.Model):
    pib = models.CharField(max_length=100)
    post = models.CharField(
        max_length=50, choices=choices, default='pharmacist')
    employ_date = models.DateField(default=timezone.now)
    email = models.EmailField(max_length=100)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Boss')

    def __str__(self):
        return f'{self.pib} ({self.post})'

    def get_post(self):
        return posts[f'{self.post}']


mptt.register(Employee)
