from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm, ReviewForm


@login_required
def booking_list_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST' and 'review_id' in request.POST:
        booking_id = request.POST.get('review_id')
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        form = ReviewForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Отзыв успешно добавлен!')
            return redirect('bookings:booking_list')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_form_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Заявка успешно отправлена на рассмотрение!')
            return redirect('bookings:booking_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def admin_dashboard_view(request):
    # Проверка прав доступа согласно ТЗ
    if not getattr(request.user, 'is_admin', False) and request.user.username != 'Conf2027' and not request.user.is_superuser:
        messages.error(request, 'У вас нет доступа к панели администратора')
        return redirect('bookings:booking_list')
    
    bookings = Booking.objects.all().order_by('-created_at')
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        new_status = request.POST.get('status')
        booking = get_object_or_404(Booking, id=booking_id)
        booking.status = new_status
        booking.save()
        messages.success(request, f'Статус заявки обновлен на "{booking.get_status_display()}"')
        return redirect('bookings:admin_dashboard')
    return render(request, 'bookings/admin_dashboard.html', {'bookings': bookings})