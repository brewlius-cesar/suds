from django.contrib import admin

from .models import Beer, Batch, PackageType, Package, Customer, Order

admin.site.register( Beer )
admin.site.register( Batch )
admin.site.register( PackageType )
admin.site.register( Package )
admin.site.register( Customer )
admin.site.register( Order )

