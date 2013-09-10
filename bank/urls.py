from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import (
    WithdrawalCreate, DepositCreate, BankHomeTemplate
)

urlpatterns = patterns('',
    url(r'^$', BankHomeTemplate.as_view(), name='bank_home'),
	url(r'^add-withdrawal/$', WithdrawalCreate.as_view(), name='withdrawal_create'),
	url(r'^add-deposit/$', DepositCreate.as_view(), name='deposit_create'),
)
