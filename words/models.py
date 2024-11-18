from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=[("en", "English"), ("ar", "Arabic")])
    level = models.IntegerField()

    def __str__(self):
        return f"{self.text} ({self.language})"
