from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        # First save image
        super().save(*args, **kwargs)

        # Check if image exists
        if self.image:
            image_path = self.image.path

            if os.path.exists(image_path):
                img = Image.open(image_path)

                # Resize if too large
                if img.height > 300 or img.width > 300:
                    img.thumbnail((300, 300))
                    img.save(image_path)