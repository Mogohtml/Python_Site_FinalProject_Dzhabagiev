from django.db import models

from core.constraints import SizeEnum, CategoryEnum
from users.models import User


# Модель Clothes
class Clothes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    material = models.CharField(max_length=100)
    size = models.CharField(max_length=11, choices=[(size.value, size.name) for size in SizeEnum])
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=[(category.value, category.name) for category in CategoryEnum])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


# Модель Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/posts/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothes = models.ManyToManyField(Clothes)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Модель RentalRequest
class RentalRequest(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Request by {self.user.email} for {self.post.title}"


# Модель Transaction
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    rental_period_start = models.DateTimeField()
    rental_period_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction by {self.user.email} for {self.post.title}"
