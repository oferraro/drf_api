from rest_framework import generics
from rest_framework.exceptions import ParseError
from .models import Transaction
from .serializers import TransactionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse


class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@method_decorator(csrf_exempt, name='transaction')
def AddTransaction(request):
    payload = json.loads(request.body.decode("utf-8"))
    if (payload["amount"] > 0):
        type='inflow'
    elif (payload["amount"] < 0):
        type='outflow'
    else:
        raise ParseError(detail='amount cant be 0')
    transaction = Transaction.objects.create(
        reference=payload["reference"],
        account=payload["account"],
        date=payload["date"],
        amount=payload["amount"]*100,
        type=type,
        category=payload["category"],
        user_id=payload["user_id"],
    )
    serializer = TransactionSerializer(transaction)
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")
