
import os

from django.db import models
from dotenv import load_dotenv
from mtnmomo.collection import Collection

from api.authentication.models import User
from api.utils.id_generatory import ID_LENGTH, id_gen

from ...manager import BaseManager
from ...models import BaseModel
from django.db.models import Max, Sum


class SavingsManager(BaseManager):
    def savings_objects(self):
        pass


class Savings(BaseModel):
    SUCCESSFUL = 'SS'
    PENDING = 'PG'
    FAILED = 'FD'
    APPROVAL_REJECTED = 'RD'
    TIMEOUT = 'TT'
    EXPIRED = 'ED'

    choices = [(SUCCESSFUL, 'Success'),
               (PENDING, 'Pending'), (FAILED, 'Failed')]

    id = models.CharField(
        max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False
    )
    saver = models.ForeignKey(
        User, related_name="saver", on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_id = models.PositiveIntegerField(default=00000)
    transaction_ref_id = models.CharField(max_length=40, null=True)
    status = models.CharField(choices=choices, max_length=2, default=PENDING)
    financial_transaction_id = models.CharField(max_length=200)

    # objects = BaseManager()

    @property
    def get_transaction_id(self):
        transaction_id = Savings.objects.aggregate(Max('transaction_id'))[
            'transaction_id__max']
        return transaction_id+1 if transaction_id else 1

    @property
    def get_total_savings(self):
        return Savings.objects.aggregate(Sum('amount'))['amount__sum']

    def get_user_total_savings(self, saver):
        return Savings.objects.filter(saver=saver).aggregate(Sum('amount'))['amount__sum']

    def __str_(self):
        return f'<{self.saver.email}-{self.amount}>'
