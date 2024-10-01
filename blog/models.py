from django.db import models

# Create your models here.
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title
