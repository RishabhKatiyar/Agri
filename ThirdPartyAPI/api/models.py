from django.db import models


class News(models.Model):
    headline = models.TextField(max_length=50)
    content = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.headline}"