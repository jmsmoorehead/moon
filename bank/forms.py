from django import forms

from .models import Transfer

class DepositForm(forms.ModelForm):

    class Meta:
        model = Transfer
        fields = ('contact', 'amount',)

    def save(self, force_insert=False, force_update=False, commit=True):
        obj = super(DepositForm, self).save(commit=False)
        if obj.amount > 0:
            obj.amount = obj.amount * -1
        obj.transfer_type = 'D'
        obj.save()
        return obj

class WithdrawalForm(forms.ModelForm):

    class Meta:
        model = Transfer
        fields = ('contact', 'amount',)
        
    def save(self, force_insert=False, force_update=False, commit=True):
        obj = super(WithdrawalForm, self).save(commit=False)
        obj.transfer_type = 'W'
        obj.save()
        return obj