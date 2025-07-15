from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.PositiveIntegerField(default=0)
    product_name = models.CharField(default="Name")
    product_description = models.TextField(default="Description")
    product_image = models.TextField(default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapers.com%2Fimages%2Fhd%2Frick-astley-th6vqytajjixfuqj.jpg&f=1&nofb=1&ipt=f19782157651bbdb301786bbb63d7b42ca4985ea7b843fdcee9dfaab1e7a7a46")

# class ProductID (models.Model):
#     product_id = models.PositiveIntegerField()
