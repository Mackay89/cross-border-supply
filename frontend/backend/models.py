
m django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
        name = models.CharField(max_length=255)
            description = models.TextField()
                price = models.DecimalField(max_digits=10, decimal_places=2)
                    stock_quantity = models.IntegerField()

                    class Order(models.Model):
                            user = models.ForeignKey(User, on_delete=models.CASCADE)
                                product = models.ForeignKey(Product, on_delete=models.CASCADE)
                                    quantity = models.IntegerField()
                                        status = models.CharField(max_length=50)
                                            total_price = models.DecimalField(max_digits=10, decimal_places=2)
                                                created_at = models.DateTimeField(auto_now_add=True)

