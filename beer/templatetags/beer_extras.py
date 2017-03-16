import re

from django import template
from django.urls import reverse
from django.conf import settings

#
# Some simple helper filters and tags, try to use capitals (upper camel-case)
# so that these stand out from built-in tags/filters
#

register = template.Library()

@register.simple_tag
def ActiveTab( request, urlname, suffix = '$' ):
    urlpattern = reverse( urlname )

    # Try to limit the match to only what's in the reversed
    # url (i.e. add leading '^' to regex search...)
    if re.search( '^' + urlpattern + suffix, request.path ):
        return 'active'

    return ''

