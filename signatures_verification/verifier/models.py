from django.db import models
from django.contrib.auth.models import User

class Signature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signature_image = models.ImageField(upload_to='signatures/',null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Signature of {self.user.username} at {self.uploaded_at}'
