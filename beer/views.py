from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import NewBatchForm
from .models import Beer, PackageType

@login_required
def summary( request ):
    ctxt = { 'beers' : [] }

    pkg_types = PackageType.objects.all()
    for bier in Beer.objects.all():
        cur_bier = { 'beer' : bier }
        pkg_counts = []
        for ptype in pkg_types:
            pkg_counts.append( ( ptype.name, 
                                 bier.packages.filter( package_type = ptype ).count() ) )

        cur_bier['pkg_counts'] = pkg_counts
        ctxt['beers'].append( cur_bier )

    return render( request, 'beer/summary.html', ctxt )

@login_required
def inventory( request, product_id = None ):
    return HttpResponseNotFound()

@login_required
def orders( request, order_id = None ):
    return HttpResponseNotFound()

@login_required
def customers( request, customer_id = None ):
    return HttpResponseNotFound()

@login_required
def new_batch( request ):
    if request.method == 'POST':
        batch_form = NewBatchForm( request.POST )
        
        if not batch_form.is_valid():
            return render( request, 
                           "beer/new_batch.html", 
                           { 'new_batch_form' : batch_form } )

        lstNewPkgs = []
        for pkgtyp in batch_form.pkgtypes:
            iCount = pkgtyp[1].cleaned_data
            for i in range( field ):
                lstNewPkgs.append( Package( package_type = pkgtyp[0],
                                            beer = batch_form.beer.cleaned_data ) )

        Package.objects.bulk_create( lstNewPkgs )
    else:
        return render( request, 
                       'beer/new_batch.html', 
                       { 'new_batch_form' : NewBatchForm() } )


