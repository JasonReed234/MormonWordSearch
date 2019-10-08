from django.db import models



class Word(models.Model):
    word_text = models.CharField(max_length=200)
