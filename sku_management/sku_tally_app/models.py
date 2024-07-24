from django.db import models

class SKU(models.Model):
    name = models.CharField(max_length=255)
    metadata = models.JSONField()

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name