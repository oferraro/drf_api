# transactions/serializers.py
from rest_framework import serializers
from . import models


class TransactionSerializer(serializers.ModelSerializer):

    amount = serializers.SerializerMethodField()

    def get_amount(self, obj):
        return "{0:.2f}".format((obj.amount/100))


    class Meta:
        fields = ('id', 'reference', 'account', 'date', 'amount', 'type', 'category', 'created_at', 'updated_at',)
        model = models.Transaction
