from django import forms

from .models import Beer, PackageType

class NewBatchForm( forms.Form ):
    PKG_TYPE_PREFIX = 'pkg-type-input-'
    beer = forms.ModelChoiceField( queryset = Beer.objects.all(),
                                   empty_label = None )

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        
        self.pkgtypes = []
        for pkg_type in PackageType.objects.all():
            cField = forms.IntegerField() 
            self.fields[self.PKG_TYPE_PREFIX + str(pkg_type.id)] = cField
            self.pkgtypes.append( (pkg_type, cField ) )


