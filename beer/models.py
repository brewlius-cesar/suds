from django.db import models

class Beer( models.Model ):
    name = models.CharField( max_length = 256 )

    def __str__( self ):
        return self.name

class Batch( models.Model ):
    date = models.DateField()
    beer = models.ForeignKey( Beer,
                              related_name = 'batches' )

class PackageType( models.Model ):
    capacity = models.FloatField()
    name = models.CharField( max_length = 256 )

    def __str__( self ):
        return self.name

class Package( models.Model ):
    batch = models.ForeignKey( Batch,
                               related_name = 'packages' )
    package_type = models.ForeignKey( PackageType )

    def __str__( self ):
        return str( self.package_type ) + ' ' + str( self.batch.beer )

class Customer( models.Model ):
    name = models.CharField( max_length = 256 )

    def __str__( self ):
        return self.name

class Order( models.Model ):
    date_placed = models.DateField()
    date_promised = models.DateField()
    date_filled = models.DateField()
    customer = models.ForeignKey( Customer,
                                  related_name = 'orders' )
    packages = models.ForeignKey( Package,
                                  related_name = 'orders' )

    def __str__( self ):
        return self.customer + ' ' + len( self.packages ) + 'Items'

