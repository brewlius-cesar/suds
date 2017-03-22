from rest_framework import serializers

from .models import ( Beer,
                      Batch,
                      PackageType,
                      Package,
                      Customer,
                      Order )


class BeerSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Beer
        fields = ( 'name', )

class BatchSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Batch
        fields = ( 'date', )

class PackageTypeSerializer( serializers.ModelSerializer ):
    class Meta:
        model = PackageType
        fields = ( 'capacity', 'name' )

class PackageSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Package
        fields = ( 'batch', 'package_type', 'beer' )

class CustomerSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Customer
        fields = ( 'name', )

class OrderSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Order
        fields = ( 'date_placed', 'date_promised', 'date_filled', 'customer', 'packages' )

