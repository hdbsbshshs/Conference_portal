from django.db import models
from django.conf import settings  # Важно: импортируем settings


class Booking(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('scheduled', 'Мероприятие назначено'),
        ('completed', 'Завершено'),
    ]

    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Банковская карта'),
        ('transfer', 'Безналичный расчет'),
    ]

    # Меняем User на settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='bookings'
    )
    room_name = models.CharField(max_length=255, verbose_name='Название помещения')
    conference_date = models.DateTimeField(verbose_name='Дата и время начала')
    payment_method = models.CharField(
        max_length=20, 
        choices=PAYMENT_CHOICES, 
        default='card', 
        verbose_name='Способ оплаты'
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new', 
        verbose_name='Статус'
    )
    review = models.TextField(blank=True, null=True, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка от {self.user} на {self.room_name}"