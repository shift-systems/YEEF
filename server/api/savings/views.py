from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Savings
from .renderers import SavingsJSONRenderer
from .serializers import SavingsSerializer
from .helpers import request_to_pay, get_transaction_status, process_response
import time


class SavingsView(APIView):
    """View to request for saving to the system
    * Requires authentication
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SavingsSerializer
    renderer_classes = (SavingsJSONRenderer,)

    def post(self, request, *args, **kwargs):

        saver = request.user
        saving = request.data.get('savings')
        payment_details = {
            # "mobile": '46733123451',
            "mobile": saver.mobile_number,
            "amount": saving['amount'],
            "external_id": Savings().get_transaction_id,
        }
        response = request_to_pay(payment_details)

        if "transaction_ref" in response.keys():
            savings_resp = get_transaction_status(response['transaction_ref'])
            while savings_resp['status'] == 'PENDING':
                time.sleep(3)
                savings_resp = get_transaction_status(
                    response['transaction_ref'])
        payment_details['saver'] = saver.id
        payment_details['transaction_ref'] = response['transaction_ref']

        savings_info = process_response(savings_resp, payment_details)
        data = savings_info
        if 'error' not in savings_info.keys():
            serializer = self.serializer_class(data=savings_info)
            serializer.is_valid(raise_exception=True)

            serializer.save()
            data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):

        saver = request.user
        savings = Savings.objects.filter(saver=saver)
        serializer = self.serializer_class(savings, many=True)
        total_savings = Savings().get_user_total_savings(saver=saver)
        data = serializer.data + [{'total_savings': float(total_savings)}]

        return Response(data=data, status=status.HTTP_200_OK)


class AllSavingsView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = SavingsSerializer
    renderer_classes = (SavingsJSONRenderer,)

    def get(self, request, *args, **kwargs):
        all_savings = Savings.objects.all()
        serialized = self.serializer_class(all_savings, many=True)
        total_savings = Savings().get_total_savings
        data = serialized.data + [{'total_savings': float(total_savings)}]
        return Response(data=data, status=status.HTTP_200_OK)
