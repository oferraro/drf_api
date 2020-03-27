from django.db import models

class Transaction(models.Model):
    reference = models.CharField(max_length=200, unique=True)
    account = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.IntegerField()
    type = models.CharField(
        max_length=32,
        choices=[('inflow', 'inflow'), ('outflow', 'outflow')],
        default='inflow'
    )
    category = models.CharField(max_length=200)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reference
