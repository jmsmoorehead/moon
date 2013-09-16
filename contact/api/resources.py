from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation


from ..models import Contact
from ..forms import ContactForm


class ContactResource(ModelResource):
    class Meta:
        resource_name = 'contact'        
        queryset = Contact.objects.all()    
        list_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        list_allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        authentication = Authentication()
        authorization = Authorization()    
        validation = FormValidation(form_class=ContactForm)
        