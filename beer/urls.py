from django.conf.urls import url, include

from rest_framework import routers

from .views import ( BeerViewSet,
                     BatchViewSet,
                     PackageTypeViewSet,
                     PackageViewSet,
                     CustomerViewSet,
                     OrderViewSet )

router = routers.DefaultRouter()
router.register( r'beer', BeerViewSet )
router.register( r'batch', BatchViewSet )
router.register( r'package-type', PackageTypeViewSet )
router.register( r'package', PackageViewSet )
router.register( r'customer', CustomerViewSet )
router.register( r'order', OrderViewSet )

urlpatterns = [
    url( r'^', include( router.urls ) ),
    url( r'^auth/', include( 'rest_framework.urls', namespace = 'rest_framework' ) ),
]

