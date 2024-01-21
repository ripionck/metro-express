from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 12)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us"