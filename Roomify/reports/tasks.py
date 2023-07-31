from celery import shared_task
from django.template.loader import render_to_string
from reservations.models import Reservation


@shared_task
def generate_report(reservation_id):
    reservation = Reservation.objects.all()
    
    context = {
        'reservation':reservation
    }
    report_html = render_to_string('report.html', context)
    report_text = render_to_string('report.txt', context)
    return {'html': report_html, 'text': report_text}