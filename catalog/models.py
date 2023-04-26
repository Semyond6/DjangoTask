from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from myweb.api.validators import (
    validator_serial_number_mask,
)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Equipment_type(models.Model):
    """Модель типа оборудования"""
    
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(
        max_length=255, 
        verbose_name='Тип оборудования',
    )
    serial_number_mask = models.CharField(
        max_length=255, 
        verbose_name='Маска SN',
        validators=[validator_serial_number_mask],
    )
    
    def __str__(self) -> str:
        return self.type_name

class Equipment(models.Model):
    """Модель оборудования"""
    
    id = models.AutoField(primary_key=True)
    equipment_type = models.ForeignKey(
        'Equipment_type', 
        verbose_name='Тип оборудования',
        on_delete=models.CASCADE,
    )
    serial_number = models.CharField(
        max_length=255, 
        verbose_name='SN',
    )
    comment = models.CharField(
        max_length=255, 
        verbose_name='Примечание',
        default='',
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['serial_number'], 
                name='unique serial'
            )
        ]