from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from tastypie import fields


from contact.api.resources import ContactResource

from ..models import Transfer
from ..forms import WithdrawalForm, DepositForm




class DepositResource(ModelResource):
    
    contact = fields.ToOneField(ContactResource, 'contact', full=True)
    
    class Meta:
        resource_name = 'deposit'        
        queryset = Transfer.deposits.all()    
        list_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        list_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        authentication = Authentication()
        authorization = Authorization()    
        validation = FormValidation(form_class=DepositForm)
        fields = ['date_created', 'amount', 'contact', 'id']
        
    def obj_create(self, bundle, **kwargs):
        bundle = super(DespositResource, self).obj_create(bundle, transfer_type='D', **kwargs)
        return bundle
        
    def dehydrate_amount(self, bundle, **kwargs):
        return bundle.obj.amount * -1   
        
class WithdrawalResource(ModelResource):
    
    contact = fields.ToOneField(ContactResource, 'contact', full=True)
    
    
    class Meta:
        resource_name = 'withdrawal'        
        queryset = Transfer.withdrawals.all()    
        list_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        list_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        authentication = Authentication()
        authorization = Authorization()    
        validation = FormValidation(form_class=WithdrawalForm)
        fields = ['date_created', 'amount', 'contact', 'id']

    def obj_create(self, bundle, **kwargs):
        bundle = super(WithdrawalResource, self).obj_create(bundle, transfer_type='W', **kwargs)
        return bundle