from datetime import date

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
    line_item = models.ForeignKey( 'OrderLineItem',
                                   related_name = 'packages',
                                   null = True,
                                   blank = True )

    def __str__( self ):
        return str( self.package_type ) + ' ' + str( self.batch.beer )

class Customer( models.Model ):
    name = models.CharField( max_length = 256 )

    def __str__( self ):
        return self.name

class OrderLineItem( models.Model ):
    package_type = models.ForeignKey( PackageType,
                                      related_name = 'line_items' )
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey( 'Order',
                               related_name = 'line_items' )
    beer = models.ForeignKey( 'Beer',
                              related_name = 'line_items' )

class Order( models.Model ):
    date_placed = models.DateField( default = date.today )
    date_promised = models.DateField()
    date_filled = models.DateField( null = True,
                                    blank = True )
    customer = models.ForeignKey( Customer,
                                  related_name = 'orders' )
    def __str__( self ):
        return self.customer + ' ' + len( self.packages ) + 'Items'

    def ItemCount( self ):
        tot_items = 0
        for line_item in self.line_items:
            tot_items += line_item.quantity


        return tot_items

