from decimal import Decimal
from django.db import models
from account.models import Customer
from author.models import AuthorProfile


class Category(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='products_category')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    inventory = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=5)
    discount_value = models.IntegerField()


class OrderDetail(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    description = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    lineOrder = models.ManyToManyField(OrderDetail)
    shipping_price = models.IntegerField(null=True, blank=True)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, null=True, blank=True)

    total = models.IntegerField(null=True, blank=True)
    ordered = models.BooleanField(default=False)

    @property
    def name(self):
        return "Testing"

    @property
    def netPaid(self):
        return self.total * 0.1

    def get_total_price(self):
        total = 0
        for order_item in self.lineOrder.all():
            total += order_item.get_total_item_price()
        return total + self.shipping_price + self.coupon.discount_value
