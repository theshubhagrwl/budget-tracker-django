from django.db import models
from api.users.models import User


class Items(models.Model):
    ITEM_TYPE = [
        ("expense", "Expense"),
        ("income", "Income"),
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField()
    data = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    itemType = models.CharField(max_length=10, choices=ITEM_TYPE)

    def __str__(self):
        return self.title
