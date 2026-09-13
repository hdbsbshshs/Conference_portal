from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room_name', 'conference_date', 'payment_method']
        widgets = {
            'conference_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'room_name': forms.TextInput(attrs={'placeholder': 'Введите название помещения'}),
        }
        labels = {
            'room_name': 'Название помещения',
            'conference_date': 'Дата и время начала конференции',
            'payment_method': 'Способ оплаты',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['review']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Оставьте ваш отзыв...'})
        }
        labels = {
            'review': 'Отзыв'
        }