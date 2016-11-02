from django.db import models

class Ticket(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=200)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.category

class Sales(models.Model):
    user = models.ForeignKey('users.User', blank=True, null=True)
    ticket = models.ForeignKey('Ticket', blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
