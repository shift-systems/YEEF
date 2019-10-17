
from django.db import models

from ...models import BaseModel
from ...manager import BaseManager
from api.authentication.models import User

from api.utils.id_generatory import id_gen, ID_LENGTH


class SavingsManager(BaseManager):
    def savings_objects(self):
        pass


class Savings(BaseModel):
    SUCCESS = 'SS'
    PENDING = 'PG'
    FAILED = 'FD'

    choices = [(SUCCESS, 'Success'), (PENDING, 'Pending'), (FAILED, 'Failed')]

    id = models.CharField(
        max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False
    )
    saver = models.ForeignKey(User,related_name="saver", on_delete=models.SET_NULL,null=True)
    amount = models.DecimalField(editable=False, max_digits =15, decimal_places=2)
    transaction_id = models.PositiveIntegerField(null=True)
    transaction_ref_id = models.CharField(max_length=40,null=True)
    status = models.CharField(choices=choices, max_length=2, default=PENDING)
    financial_transaction_id = models.PositiveIntegerField(null=True)

    objects = BaseManager()

    def __str_(self):
        return f'<{self.saver.email}-{self.amount}>'
