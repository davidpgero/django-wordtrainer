from django.db import models
from django.contrib import auth

class WordList(models.Model):
    """ A word list contains word pairs. """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class WordPair(models.Model):
    """ Word Pairs with challenge and response. """
    word_list = models.ForeignKey(WordList)
    prompt = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class TrainingItem(models.Model):
    """ Keeps track of pairs in training. """
    user = models.ForeignKey(auth.models.User)
    word_pair = models.ForeignKey(WordList)
    repetitions = models.IntegerField(default=0)
    mistakes = models.IntegerField(default=0)
