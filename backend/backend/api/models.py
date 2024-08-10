from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
  title = models.CharField(max_length=255)
  amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Entry")

  def __str__(self) -> str:
    return self.title