# Create your views here.
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.db.models import Sum
from django.core.urlresolvers import reverse


from braces.views import FormValidMessageMixin
from contact.models import Contact

from .forms import WithdrawalForm, DepositForm
from .models import Transfer

class BankHomeTemplate(TemplateView):
    template_name = "bank/bank_home.html"
    
    def get_context_data(self, **kwargs):
        context = super(BankHomeTemplate, self).get_context_data(**kwargs)

        context['withdrawls'] = Transfer.withdrawals.all()[:5]
        context['deposits'] = Transfer.deposits.all()[:5]
        context['current_balance'] = Transfer.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0.00
        
        contacts = Contact.objects.all().annotate(amount = Sum('transfer__amount'))


        context['contacts_owed'] = filter(lambda i: i.amount is not None and i.amount > 0, contacts)
        context['contacts_owe'] = filter(lambda i: i.amount is not None and i.amount < 0, contacts)
        return context

class WithdrawalCreate(FormValidMessageMixin, CreateView):
    model = Transfer
    form_class = WithdrawalForm
    template_name = "bank/withdrawal_create.html"
    form_valid_message = 'Withdrawal created!'

    def get_success_url(self):
		return reverse('bank_home')    

class DepositCreate(FormValidMessageMixin, CreateView):
    model = Transfer
    form_class = DepositForm
    template_name = "bank/deposit_create.html"
    form_valid_message = 'Deposit created!'
    
    def get_success_url(self):
		return reverse('bank_home')