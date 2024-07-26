from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"  
    

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveBigIntegerField()
    description = models.TextField(max_length=1000, null = True, blank = True)
    image = models.ImageField(upload_to="product_images")
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.name}"
    

class Cart(models.Model):
    product =models.OneToOneField(Product, on_delete =models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product.name


