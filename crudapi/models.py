from django.db import models

# Create your models here.
class ItemList(models.Model):
    # different types of category like electronic ,furniture,clothing,groceries depend upon their company and product list
    category = models.CharField(max_length=300)
    sub_category = models.CharField(max_length=400)
    item_name = models.CharField(max_length=255)
    item_location = models.CharField(max_length=300)
    item_id = models.CharField(max_length=25)
    item_description = models.TextField()
    item_amount = models.PositiveIntegerField()
    def __str__(self) -> str:
        return f"{self.item_name} is the best product from our company"
    





