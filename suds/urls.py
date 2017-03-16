"""suds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.shortcuts import redirect

import beer.views

urlpatterns = [
    url( r'^nimda/', admin.site.urls ),
    url( r'^admin/$', lambda x: redirect( 'nimda/' ), name='admin' ),

    url( r'^$', lambda x: redirect( 'beer/' ) ),
    url( r'^beer/$', beer.views.summary, name='summary' ),
    url( r'^beer/login/$', login, {'template_name' : 'beer/login.html'}, name = 'login' ),
    url( r'^beer/logout/$', logout, { 'next_page': '/beer/login/' }, name = 'logout' ),
    url( r'^beer/inventory/$', beer.views.inventory, name='inventorylist' ),
    url( r'^beer/newbatch/$', beer.views.new_batch, name='newbatch' ),
    url( r'^beer/inventory/(?P<product_id>[0-9]*)/$', beer.views.inventory, name='inventory' ),
    url( r'^beer/orders/$', beer.views.orders, name='orders' ),
    url( r'^beer/orders/(?P<order_id>[0-9]*)/$', beer.views.orders, name='order' ),
    url( r'^beer/customers/$', beer.views.customers, name='customers' ),
    url( r'^beer/customers/(?P<customer_id>[0-9]*)/$', beer.views.customers, name='customer' ),
]


