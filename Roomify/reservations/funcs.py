
from .models import Reservation


def is_free(valid_data):
    reservations = Reservation.objects.filter(room=valid_data['room'])
    if valid_data['start_date'] <= valid_data['end_date']:
        for reservation in reservations:
            print(valid_data['start_date'], valid_data['end_date'], reservation.start_date, reservation.end_date)
            if valid_data['start_date'] >= reservation.start_date and valid_data['start_date'] <= reservation.end_date:
                return False
            if valid_data['end_date'] <= reservation.end_date and valid_data['end_date'] >= reservation.start_date:
                return False
        return True
    else:
        False