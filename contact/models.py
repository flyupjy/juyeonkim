from django.db import models

# Create your models here.
class Contact(models.Model):
    sender = models.EmailField(max_length=128)
    subject = models.CharField(max_length=128)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender