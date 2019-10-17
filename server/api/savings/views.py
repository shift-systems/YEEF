import os
import logging
from dotenv import load_dotenv
from mtnmomo.collection import Collection
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Savings, User
from .renderers import SavingsJSONRenderer
from .serializers import SavingsSerializer

load_dotenv()

client = Collection({
    "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
    "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
    "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
})


def request_to_pay(payment_details):
    pay_request = client.requestToPay(
        payee_note="Thanks for Saving", payer_message="dd", currency="EUR", **payment_details
    )

    return pay_request


def get_transaction_status(transaction_ref):
    get_request_transaction = client.getTransactionStatus(transaction_ref)
    return get_request_transaction


class SavingsView(APIView):
    """View to request for saving to the system
    * Requires authentication
    """
    permission_classes = (AllowAny, IsAuthenticated)
    serializer_class = SavingsSerializer
    renderer_classes = (SavingsJSONRenderer,)

    def post(self, request, *args, **kwargs):

        saver = request.user
        saving = request.data.get('savings')
        saving['saver'] = saver.id
        amount = saving['amount']
        user_mobile = saver.mobile_number
        payment_details = {
            "mobile": "256"+str(user_mobile), "amount": str(amount), "external_id": "1234567654"
        }
        response = request_to_pay(payment_details)
        if "transaction_ref" in response.keys():
            ret_response = get_transaction_status(response['transaction_ref'])
        saving['transaction_ref_id'] = response['transaction_ref']
        saving['financial_transaction_id'] = ret_response['financialTransactionId']
        if ret_response['status']:
            saving['status'] = Savings.SUCCESSFUL
        serializer = self.serializer_class(data=saving)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
