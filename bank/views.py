# Create your views here.
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.db.models import Sum
from django.core.urlresolvers import reverse


from braces.views import FormValidMessageMixin
from contact.models import Contact

from .forms import WithdrawalForm, DepositForm
from .models import Withdrawal, Deposit
from .utils import get_total_owed, get_owed, get_owe

class BankHomeTemplate(TemplateView):
    template_name = "bank/bank_home.html"
    
    def get_context_data(self, **kwargs):
        context = super(BankHomeTemplate, self).get_context_data(**kwargs)
        withdrawn = Withdrawal.objects.all().aggregate(Sum('amount'))['amount__sum']
        deposited = Deposit.objects.all().aggregate(Sum('amount'))['amount__sum']
            
        context['withdrawls'] = Withdrawal.objects.all()[:5]
        context['deposits'] = Deposit.objects.all()[:5]
        context['current_balance'] = (withdrawn or 0) - (deposited or 0)
        
        contacts_withdrawal = Contact.objects.all().annotate(w_amount = Sum('withdrawal__amount')).order_by('id')
        contacts_deposit = Contact.objects.all().annotate(d_amount=Sum('deposit__amount')).order_by('id')
        contacts = get_total_owed(contacts_withdrawal, contacts_deposit)


        context['contacts'] = contacts
        context['contacts_owed'] = filter(get_owed, contacts)
        context['contacts_owe'] = filter(get_owe, contacts)
        return context

class WithdrawalCreate(FormValidMessageMixin, CreateView):
    model = Withdrawal
    form_class = WithdrawalForm
    template_name = "bank/withdrawal_create.html"
    form_valid_message = 'Withdrawal created!'

    def get_success_url(self):
		return reverse('bank_home')    

class DepositCreate(FormValidMessageMixin, CreateView):
    model = Deposit
    form_class = DepositForm
    template_name = "bank/deposit_create.html"
    form_valid_message = 'Deposit created!'
    
    def get_success_url(self):
		return reverse('bank_home')