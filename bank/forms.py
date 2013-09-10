from django import forms

from .models import Withdrawal, Deposit

class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        fields = ('contact', 'amount',)

class WithdrawalForm(forms.ModelForm):

    class Meta:
        model = Withdrawal
        fields = ('contact', 'amount',)
