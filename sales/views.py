from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer


class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SaleSerializer

    def get_queryset(self):
        queryset = Sale.objects.all()
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        product = self.request.query_params.get("product")

        # maior ou igual start_date ou menor ou igual end_date
        if start_date:
            # maior ou igual ao start_date
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            # menor ou igual ao end_date
            queryset = queryset.filter(date__lte=end_date)

        if start_date and end_date:
            # maior ou igual a start_date e menor ou igual a end_date
            queryset = queryset.filter(date__range=[start_date, end_date])

        if product:
            # se contiver product
            queryset = queryset.filter(product__icontains=product)

        return queryset

    # localhost:8000/api/sales
