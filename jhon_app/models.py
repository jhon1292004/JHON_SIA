from django.db import models


class MovieVerse(models.Model):
    title_id = models.AutoField(primary_key=True)
    title_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    rating = models.FloatField()

    def __str__(self):
        return self.title_name