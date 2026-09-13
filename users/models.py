from django.contrib.auth.models import AbstractUser
from django.db import models
import re
def validate_phone(value):
    pattern = r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$'
    if not re.match(pattern, value):
        raise ValueError('Телефон должен быть в формате 8(XXX)XXX-XX-XX')
    
def validate_cyrillic(value):
    if not all(c.isalpha() or c.isspace() for c in value):
        raise ValueError('ФИО должно содержать только символы кириллицы и пробелы')
    
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Логин',
        help_text='Только латиница и цифры, не менее 6 символов' 
    )
    password = models.CharField(
        max_length=128,
        verbose_name='Пароль'
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        validators=[validate_cyrillic]
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        validators=[validate_phone]
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Электронная почта'
    )
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='Specific permissions for this user.'
    )
    user_permissions = models.ManyToManyField(
            'auth.Permission',
            related_name='customuser_set',
            blank=True,
            verbose_name='user permission',
            help_text='Specific permissions for this user.'
        )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        