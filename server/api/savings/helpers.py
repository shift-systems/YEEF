
import os
import logging
from mtnmomo.collection import Collection
from .models import Savings

client = Collection({
    "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
    "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
    "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
})

statuses = {'SUCCESSFUL': Savings.SUCCESSFUL, 'FAILED': Savings.FAILED, 'EXPIRED': Savings.EXPIRED,
            'APPROVAL_REJECTED': Savings.APPROVAL_REJECTED, 'TIMEOUT': Savings.TIMEOUT}


def request_to_pay(payment_details):
    pay_request = client.requestToPay(
        payee_note="Thanks for Saving",
        payer_message="dd", currency="EUR",
        **payment_details
    )

    return pay_request


def get_transaction_status(transaction_ref):
    get_request_transaction\
        = client.getTransactionStatus(transaction_ref)
    return get_request_transaction


def process_response(saving_data, payment_details):

    status = saving_data['status']

    if status != 'SUCCESSFUL':
        return {'error': 'Transaction not successfull please try again',
                'reason': saving_data['reason']}

    saving_info = {
        'saver': payment_details['saver'],
        'amount': payment_details['amount'],
        'transaction_ref_id': payment_details['transaction_ref'],
        'financial_transaction_id': saving_data['financialTransactionId'],
        'status': statuses[status],
        'transaction_id': payment_details['external_id'],
    }
    return saving_info
