from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.views.generic import TemplateView

from tastypie.api import Api


from contact.api.resources import ContactResource
from bank.api.resources import WithdrawalResource, DepositResource


v1_api = Api(api_name='v1')
v1_api.register(ContactResource())
v1_api.register(WithdrawalResource())
v1_api.register(DepositResource())

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'borrow_money.views.home', name='home'),
    # url(r'^borrow_money/', include('borrow_money.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home_page'),
	
        
    url(r'^contact/', include('contact.urls')),    
    url(r'^bank/', include('bank.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    
)
