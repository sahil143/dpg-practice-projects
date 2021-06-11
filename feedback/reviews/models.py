from django.db import models

# Create your models here.
class Review(models.Model):

    user_name = models.CharField(max_length=10)
    review_text = models.TextField()
    rating = models.IntegerField()
    owner_comment = models.TextField()

    def __str__(self):
        return self.user_name

