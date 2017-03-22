from rest_framework import viewsets

from .models import ( Beer,
                      Batch,
                      PackageType,
                      Package,
                      Customer,
                      Order )

from .serializers import ( BeerSerializer,
                           BatchSerializer,
                           PackageTypeSerializer,
                           PackageSerializer,
                           CustomerSerializer,
                           OrderSerializer )

class BeerViewSet( viewsets.ModelViewSet ):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class BatchViewSet( viewsets.ModelViewSet ):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class PackageTypeViewSet( viewsets.ModelViewSet ):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeSerializer

class PackageViewSet( viewsets.ModelViewSet ):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class CustomerViewSet( viewsets.ModelViewSet ):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet( viewsets.ModelViewSet ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

