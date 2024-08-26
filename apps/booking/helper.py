from django.db.models import Q
from .models import Bookings


def is_slot_available(service, booking_date, start_time, end_time):
    # Check if any bookings overlap with the requested time slot
    overlapping_bookings = Bookings.objects.filter(
        Q(service=service) &
        Q(booking_date=booking_date) &
        Q(start_time__lt=end_time) &  # start time of existing booking is before end time of new booking
        Q(end_time__gt=start_time)  # end time of existing booking is after start time of new booking
    ).exists()
    return overlapping_bookings
