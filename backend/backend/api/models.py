from django.db import models

# Create your models here.
class Entry(models.Model):
  title = models.CharField(max_length=255)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.title} - {self.amount}"