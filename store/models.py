from django.db import models


class Product(models.Model):
    title = models.TextField(max_length=255)
    description = models.CharField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField()


class Customer(models.Modle):
    class MembershipChoices(models.TextChoices):
        BRONZE = "B", "Bronze"
        SILVER = "S", "Silver"
        GOLD = "G", "Gold"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.TextField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        choices=MembershipChoices.choices, default=MembershipChoices.BRONZE
    )


class Order(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = "P", "Pending"
        COMPLETE = "C", "Complete"
        FAILED = "F", "Failed"

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=255, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )

class Adress(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
