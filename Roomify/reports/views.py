from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from listings.models import Listing
from .tasks import generate_report


class ReportView(generics.GenericAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['room__listing__id']
    search_fields = ['name']

    def get(self, request, listing_id):
        listing = Listing.objects.get(id=listing_id)
        report_type = request.query_params.get('report_type', 'html')
        if report_type == 'html':
            task = generate_report.delay(listing.id)
            html = task.get(timeout=3)
            return Response(html, status=status.HTTP_200_OK)
                    
        elif report_type == 'text':
            report = generate_report(listing.id)
            return Response(report, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid report type'}, status=status.HTTP_400_BAD_REQUEST)